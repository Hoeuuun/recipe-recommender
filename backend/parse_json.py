import json
from typing import List, Dict


def get_data(json_file: str) -> List[Dict]:
    """
    Opens and reads JSON data file,
    adding each line (recipe object) to list of recipes
    """
    recipes = []

    with open(json_file, 'r') as data_file:
        for line in data_file:
            recipe = json.loads(line)
            recipes.append(recipe)

    return recipes


def remove_duplicates(recipe_list: List[Dict]) -> List:
    """ Removes recipes with duplicate titles """
    new_recipe_list = []
    seen = set()

    for recipe in recipe_list:
        if recipe['title'] not in seen:
            seen.add(recipe['title'])
            new_recipe_list.append(recipe)

    return new_recipe_list

