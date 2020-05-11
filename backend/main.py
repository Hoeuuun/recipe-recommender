from flask_sqlalchemy import Model
from backend.model import Recipe, db, RecipeStep
from typing import List


def insert_recipe(title, rating, review, time, description) -> None:
    """ Adds a new recipe """
    steps = [RecipeStep(step_num=1, instruction='Mix everything together'),
             RecipeStep(step_num=2, instruction='Pour batter and cook.')]
    recipe = Recipe(title=title, rating=rating, review=review, time=time, description=description, steps=steps)

    db.session.add(recipe)
    db.session.commit()


def delete_recipe(recipe_id: int) -> None:
    """ Deletes a recipe by its id """
    Recipe.query.filter(Recipe.id == recipe_id).delete()
    db.session.commit()

def find_recipe(recipe_id: int) -> Recipe:
    """ Finds a recipe by its id """
    recipe = Recipe.query.filter(Recipe.id == recipe_id).one()
    print("found recipe with id:", recipe_id)
    print(recipe.title)
    return recipe


def main():
    insert_recipe('Tasty Pancakes', 4, 100, 15, 'These pancakes are yummy')
    delete_recipe(1)
    find_recipe(2)
    print('all goood')


if __name__ == "__main__":
    main()
