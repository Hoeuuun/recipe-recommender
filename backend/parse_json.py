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
    Removes recipes with duplicate titles
    :return: a new list, containing only unique recipes
    """
    unique_recipe_list = []
    seen = set()

    for recipe in recipe_list:
        if recipe['title'] not in seen:
            seen.add(recipe['title'])
            unique_recipe_list.append(recipe)

    return unique_recipe_list

