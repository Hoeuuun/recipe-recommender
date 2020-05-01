import sqlite3
import re
import pickle

from ingredients_index import search_recipes_by_ingredient_words


def main():
    print("\n*** Recipe Generator ***\n")

    user_ingredients = get_ingredients()
    print("Will search for ", user_ingredients);

    conn = sqlite3.connect('data.db')

    recipe_list = search_by_ingredients(conn, user_ingredients, pickle.load(open('ingredient_index.pickle', 'rb')))

    recipes_sorted = sort_recipes_by_ingredient_count(recipe_list)

    for recipe in recipes_sorted:
        print(len(recipe['ingredients']), recipe)

    conn.close()


def search_by_ingredients(connection, ingredient_names, ingredient_index=None):
    recipe_ids = search_recipes_by_ingredient_words(ingredient_index, ingredient_names)

    recipe_list = get_recipe_list(connection, recipe_ids)

    return recipe_list


def sort_recipes_by_ingredient_count(recipe_list):
    return sorted(recipe_list, key=lambda i: len(i['ingredients']))


def get_recipe_list(conn, recipe_ids):
    recipe_list = []

    if recipe_ids is None:
        return recipe_list

    for recipe_id in recipe_ids:
        recipe = get_recipe_by_id(conn, recipe_id)
        recipe_list.append(recipe)

    return recipe_list


def get_recipe_by_id(conn, id):
    cursor = conn.cursor()
    query = f"""
        SELECT * FROM Recipe
                        JOIN RecipeIngredients 
                            ON Recipe.id = RecipeIngredients.recipeId
                        JOIN Ingredient 
                            ON RecipeIngredients.ingredientId = Ingredient.id
                        WHERE Recipe.id = {id};
        """
    #print(query)
    cursor.execute(query)

    recipes = cursor.fetchall()

    for recipe in recipes:
        id = recipe[0]
        title = recipe[1]
        rating = recipe[2]
        review_count = recipe[3]
        time = recipe[4]
        image = recipe[5]
        url = recipe[6]
        description = recipe[7]

        quantity = recipe[10]

        ingredients = []

        for ing in recipes:
            ingredients.append(ing[16])

    recipe_object = {'id': id, 'title': title, 'rating': rating, 'review_count': review_count,
                     'time': time, 'image': image, 'url': url, 'description': description,
                     'quantity': quantity, 'ingredients': ingredients}

    return recipe_object


def get_ingredients():
    user_ingredients = []
    user_input = input("Search for recipes by ingredients you already have!\n"
                       "Please enter ingredients separated with commas: ")

    user_input = re.sub('\s+', ' ', user_input).strip()

    print("\nAwesome! Searching for recipes with " + user_input + "...\n")

    for ingredient in user_input.split(','):
        user_ingredients.append(ingredient.strip())

    return user_ingredients


if __name__ == "__main__":
    main()
