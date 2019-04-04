import sqlite3
from sqlite3 import OperationalError

from parseJSON import get_data, remove_duplicates


# def find_recipes_by_ingredients(connection, ingredient_needles):
#     cursor = connection.cursor()
#
#     ingredient_ids = []
#
#     for ingredient_needle in ingredient_needles:
#         cursor.execute("SELECT id from Ingredient WHERE name LIKE ?", ["%" + ingredient_needle + "%"])
#         ingredient_ids.append(str(cursor.fetchone()[0]))
#
#     print(','.join(ingredient_ids))
#
#     cursor.execute("SELECT recipeId FROM RecipeIngredients WHERE ingredientId IN (%s)" % ','.join(ingredient_ids))
#     recipe_ids = list(map(lambda x: x[0], cursor.fetchall()))
#
#     print(recipe_ids)


def insert_new_recipe(connection, data):
    cursor = connection.cursor()
    title = data['title']
    rating = int((data['rating_stars'] / 5) * 100)
    time = data['total_time_minutes']
    url = data['url']
    image = data['photo_url']
    if image:
        image = "/".join(image.split("/")[-2:])

    cursor.execute("INSERT INTO Recipe (title, rating, time, image, url) VALUES(?, ?, ?, ?, ?)",
                   (title, rating, time, image, url))

    cursor.execute("SELECT id FROM Recipe WHERE title=?", [title])

    recipe_id = cursor.fetchone()[0]

    # print("new recipe ", recipe_id)

    seen_ingredients = set()

    for ingredient in data['ingredients']:
        ingredient_name = ingredient
        ingredient_quantity = "nan"

        cursor.execute("SELECT id FROM Ingredient WHERE name=?", [ingredient_name])
        ingredient_id = cursor.fetchone()
        if not ingredient_id:
            cursor.execute("INSERT INTO Ingredient (name) VALUES (?)", [ingredient_name])
            cursor.execute("SELECT id FROM Ingredient WHERE name=?", [ingredient_name])
            ingredient_id = cursor.fetchone()[0]
        else:
            ingredient_id = ingredient_id[0]

        if ingredient_id in seen_ingredients:
            continue

        seen_ingredients.add(ingredient_id)

        # print("new ingredient", ingredient_id, ingredient_name)

        cursor.execute("INSERT INTO RecipeIngredients (recipeId, ingredientId, quantity) VALUES (?, ?, ?)", [recipe_id,
                                                                                                             ingredient_id,
                                                                                                             0])

    for i, instruction in enumerate(data['instructions']):
        cursor.execute("INSERT INTO RecipeSteps (recipeId, stepNumber, description) VALUES (?, ?, ?)", [recipe_id, i,
                                                                                                        instruction])


# Create a connection object that represents the database
conn = sqlite3.connect('data.db')

# Create a cursor object
c = conn.cursor()

# Get the commands from data.sql file
with open('data.sql', 'r') as in_file:  # open and read the file
    sql_file = in_file.read()
sql_commands = sql_file.split(';')  # get all the commands, separated by ';'

# Execute all the commands from the file
for command in sql_commands:
    try:
        c.execute(command)
    except OperationalError as err:
        print('Skipped: ', err)

# Populate the database with data from JSON file

recipes_original = get_data('data/allrecipes/data/recipes.json')  # get the data
recipes = remove_duplicates(recipes_original)  # clean the data

for i, recipe in enumerate(recipes):
    insert_new_recipe(conn, recipe)
    if i % 10000 == 0:
        conn.commit()

# Save the changes
conn.commit()


# find_recipes_by_ingredients(conn, ["eggs", "milk"])

# Close the connection
conn.close()

print('all good')
