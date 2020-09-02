import json
from typing import List, Dict


def get_data(json_file: str) -> List[Dict]:
    """
    Opens and reads JSON data file,
    adding each line (recipe object) to list of recipes
    :return: a list of recipe dictionaries
    """
    recipes = []

    with open(json_file, 'r') as data_file:
        for line in data_file:
            recipe = json.loads(line)
            recipes.append(recipe)

    return recipes


def remove_duplicates(recipe_list: List[Dict]) -> List[Dict]:
    """
    Removes recipes with duplicate titles and descriptions
    :return: a new list, containing only unique recipes
    """
    unique_recipe_list = []
    seen = set()    # set of tuples, set{(recipe_title, recipe_description), ...}

    for recipe in recipe_list:
        title_description = (recipe['title'], recipe['description'])
        if title_description not in seen:
            seen.add(title_description)
            unique_recipe_list.append(recipe)

    return unique_recipe_list

