import sqlite3
import re
import json

from ingredients_index import search_recipes_by_ingredient_words


def main():
    print("\n*** Recipe Generator ***\n")

    user_ingredients = get_ingredients()

    conn = sqlite3.connect('data.db')

    recipe_ids = find_recipes_by_ingredients(conn, user_ingredients)

    recipe_list = get_recipe_list(conn, recipe_ids)

    # sorts the recipe list by least amount of ingredients needed
    recipes_sorted = sort_recipes_by_ingredient_count(recipe_list)

    for recipe in recipes_sorted:
        print(len(recipe['ingredients']), recipe)

    conn.close()

    # # TODO: write to json file with json.dump()
    # '''
    # import json
    # data = json.dumps(recipes_sorted)
    # with open("recipes_out.json","w") as f:
    #   f.write(data)
    # '''


def search_by_ingredients(connection, ingredient_names, ingredient_index=None):
    if ingredient_index is None:
        recipe_ids = find_recipes_by_ingredients(connection, ingredient_names)
    else:
        print("USING INDEX")
        recipe_ids = search_recipes_by_ingredient_words(ingredient_index, ingredient_names)

    recipe_list = get_recipe_list(connection, recipe_ids)

    recipes_sorted = sort_recipes_by_ingredient_count(recipe_list)

    return recipes_sorted


def sort_recipes_by_ingredient_count(recipe_list):
    return sorted(recipe_list, key=lambda i: len(i['ingredients']))


def get_recipe_list(conn, recipe_ids):
    recipe_list = []

    for recipe_id in recipe_ids:
        recipe = get_recipe_by_id(conn, recipe_id)
        recipe_list.append(recipe)

    return recipe_list


def get_recipe_by_id(conn, id):
    cursor = conn.cursor()

    cursor.execute(f"""SELECT * FROM Recipe
                        JOIN RecipeIngredients 
                            ON Recipe.id = RecipeIngredients.recipeId
                        JOIN Ingredient 
                            ON RecipeIngredients.ingredientId = Ingredient.id
                        WHERE Recipe.id = {id};""")

    recipes = cursor.fetchall()

    for recipe in recipes:
        # print(recipe)

        # 54	Beer Bread I	90	0	250x250/114163.jpg	http://allrecipes.com/Recipe/6717/	54	113	0	113	3 tablespoons white sugar
        # 54	Beer Bread I	90	0	250x250/114163.jpg	http://allrecipes.com/Recipe/6717/	54	314	0	314	1 (12 fluid ounce) can or bottle beer
        # 54	Beer Bread I	90	0	250x250/114163.jpg	http://allrecipes.com/Recipe/6717/	54	315	0	315	3 cups self-rising flour

        id = recipe[0]
        title = recipe[1]
        rating = recipe[2]
        time = recipe[3]
        image = recipe[4]
        url = recipe[5]

        quantity = recipe[8]

        ingredients = []

        for ing in recipes:
            ingredients.append(ing[10])

    recipe_object = {'id': id, 'title': title, 'rating': rating, 'time': time, 'image': image, 'url': url,
                     'quantity': quantity, 'ingredients': ingredients}

    return recipe_object


def find_recipes_by_ingredients(connection, user_ingredients):
    list_size = len(user_ingredients)

    cursor = connection.cursor()

    # Deletes view if it already exists
    for i in range(list_size):
        cursor.execute(f"DROP VIEW IF EXISTS view_recipes_with_ing_{i};")

    # cursor.execute("DROP VIEW IF EXISTS view_recipes_with_ing_0;")
    # cursor.execute("DROP VIEW IF EXISTS view_recipes_with_ing_1;")
    # cursor.execute("DROP VIEW IF EXISTS view_recipes_with_ing_2;")

    first = "0"

    # first ingredient from list
    cursor.execute(f"""CREATE VIEW view_recipes_with_ing_{first} AS
                        SELECT * FROM Recipe
                        JOIN RecipeIngredients
                            ON RecipeIngredients.recipeId=Recipe.id
                        JOIN Ingredient
                            ON Ingredient.id=RecipeIngredients.ingredientId
                        WHERE Ingredient.name LIKE '%{user_ingredients[0]}'
                        GROUP BY Recipe.id;""")

    user_ingredients.pop(0)

    for i, ingredient in enumerate(user_ingredients, 1):
        prev_view = "prev_view"
        sql_command = f"""CREATE VIEW view_recipes_with_ing_{i} AS
                            SELECT * FROM view_recipes_with_ing_{first} {prev_view}
                            JOIN RecipeIngredients
                                 ON RecipeIngredients.recipeId={prev_view}.id
                            JOIN Ingredient
                                 ON Ingredient.id= RecipeIngredients.ingredientId
                            WHERE Ingredient.name LIKE '%{ingredient}'
                            GROUP BY {prev_view}.id;"""
        # print(sql_command)

        cursor.execute(sql_command)

        cursor.execute(f"""SELECT * FROM view_recipes_with_ing_{i};""")

    last = str(list_size - 1)
    recipe_ids = []

    for row in cursor.execute(f"SELECT recipeID FROM view_recipes_with_ing_{last}"):
        recipe_ids.append(row[0])

    # print(recipe_ids)

    return recipe_ids


def get_ingredients():
    user_ingredients = []
    user_input = input("Search for recipes by ingredients you already have!\n"
                       "Please enter ingredients separated with commas: ")

    # replaces 1 or more white spaces with a single space
    user_input = re.sub('\s+', ' ', user_input).strip()

    print("\nAwesome! Searching for recipes with " + user_input + "...\n")

    for ingredient in user_input.split(','):
        # print(ingredient)
        user_ingredients.append(ingredient)

    return user_ingredients


if __name__ == "__main__":
    main()
