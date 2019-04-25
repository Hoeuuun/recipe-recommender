import json

'''
Part 1: Converting from JSON to Python
'''


def get_data(json_file):
    """
    Opens and reads JSON data file, adding each line (recipe) to list
    of recipes

    parameters:
        - json_file (string): the path/location of the input data file

    returns:
        - recipes (list): a list of recipes; each recipe is a dictionary
    """
    recipes = []

    with open(json_file, 'r') as data_file:
        for line in data_file:
            recipe = json.load(line)
            recipes.append(recipe)

    return recipes


'''
Part 2: Cleaning the Data
'''


def remove_duplicates(recipe_list):
    """
    Removes duplicates (i.e., recipes with the same title)

    parameters:
        - recipe_list (list): the original recipe list

    return value:
        - new_recipe_list (list): a new recipe list with duplicates removed
    """
    new_recipe_list = []
    seen = set()

    for recipe in recipe_list:
        if recipe['title'] not in seen:
            seen.add(recipe['title'])
            new_recipe_list.append(recipe)

    return new_recipe_list


def display_recipes(recipe_list):
    """
    Displays the recipes

    parameters:
        - recipeList (list): a list containing all the recipes by recipe's title

    return value:
        - none
    """
    for recipe in recipe_list:
        print(recipe['title'])
