import sqlite3
from sqlite3 import OperationalError
from quantulum3 import parser

from backend.parse_json import get_data, remove_duplicates
from backend.quantities import convert_to_mL


def insert_new_recipe(connection, data):
    # Create a cursor object
    cursor = connection.cursor()

    # Extract some values from json and assign to new variables
    title = data['title']
    rating = int((data['rating_stars'] / 5) * 100)
    review_count = int(data['review_count'])
    time = data['total_time_minutes']
    url = data['url']
    image = data['photo_url']
    description = data['description']

    # Pics are stored as: "photo_url":"http://images.media-allrecipes.com/userphotos/560x315/582853.jpg"
    # need only the last two values, size and name (560x315/582853.jpg)
    if image:
        image = "/".join(image.split("/")[-2:])

    # Add the values into the database
    cursor.execute("INSERT INTO Recipe (title, rating, review_count, time, image, url, description) VALUES(?, ?, ?, ?, ?, ?, ?)",
                   (title, rating, review_count, time, image, url, description))

    # Search for the recipe's title
    cursor.execute("SELECT id FROM Recipe WHERE title=?", [title])

    # Get the recipe's id, located in the first column
    recipe_id = cursor.fetchone()[0]
    data['id'] = recipe_id

    # Create a set to ensure we add only unique ingredients
    seen_ingredients = set()

    # Parse ingredients' quantity
    ingredient_quantity = 'NA'
    ingredient_value = 0.0
    ingredient_unit = 'NA'
    ingredient_entity = 'NA'
    quant_mL = 0.0

    for ingredient in data['ingredients']:
        ingredient_name = ingredient

        try:
            quant = parser.parse(ingredient_name)
        except KeyError:
            quant = []
        # make sure the quantity is not empty
        if len(quant) > 0:
            ingredient_quantity = quant[0].surface
            ingredient_value = quant[0].value
            ingredient_unit = quant[0].unit.name
            ingredient_entity = quant[0].unit.entity.name

            quant_mL = convert_to_mL(ingredient_value, ingredient_unit)

        # For each ingredient, get the its id
        cursor.execute("SELECT id FROM Ingredient WHERE name=?", [ingredient_name])
        ingredient_id = cursor.fetchone()
        # If no id found, add it for the first time, then get its id
        if not ingredient_id:
            cursor.execute("INSERT INTO Ingredient (name) VALUES (?)", [ingredient_name])
            cursor.execute("SELECT id FROM Ingredient WHERE name=?", [ingredient_name])
            ingredient_id = cursor.fetchone()[0]
        else:
            ingredient_id = ingredient_id[0]

        # Skip if we already have the ingredient_id
        if ingredient_id in seen_ingredients:
            continue

        # Else, add this id to seen ingredients set
        seen_ingredients.add(ingredient_id)

        # Add the recipe and ingredient's ids to the RecipeIngredients table
        cursor.execute(
            "INSERT INTO RecipeIngredients (recipeId, ingredientId, quantity, value, unit, entity, quant_mL) VALUES ("
            "?, ?, ?, ?, ?, ?, ?)",
            [recipe_id,
             ingredient_id,
             ingredient_quantity,
             ingredient_value,
             ingredient_unit,
             ingredient_entity,
             quant_mL])

    # Look through the steps for the recipe and add it each step to the RecipeSteps table
    for i, instruction in enumerate(data['instructions']):
        cursor.execute("INSERT INTO RecipeSteps (recipeId, stepNumber, instruction) VALUES (?, ?, ?)", [recipe_id, i,
                                                                                                        instruction])


# Create a connection object that represents the database
conn = sqlite3.connect('data.db')

# Create another cursor object
c = conn.cursor()

# Get the commands from data.sql file to create the tables
with open('data.sql', 'r') as in_file:
    sql_file = in_file.read()
sql_commands = sql_file.split(';')

# Try to execute all the commands from the file
for command in sql_commands:
    try:
        c.execute(command)
    except OperationalError as err:
        print('Skipped: ', err)

# Get and clean the data
recipes_original = get_data('../data/allrecipes/data/recipes.json')
recipes = remove_duplicates(recipes_original)

# Populate the database with data from JSON file

# Iterate through all the recipes and insert them into the database
for i, recipe in enumerate(recipes):
    insert_new_recipe(conn, recipe)

# Save the changes
conn.commit()

# Close the connection
conn.close()

# By now, if no errors, success
print('all good')


