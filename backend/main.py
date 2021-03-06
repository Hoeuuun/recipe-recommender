from flask_sqlalchemy import Model
from backend.model import Recipe, db, RecipeStep, Ingredient, RecipeIngredient
from typing import List, Tuple

from sqlalchemy import join


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


def create_ingredient(name) -> Ingredient:
    """ Creates an ingredient"""
    ing = Ingredient(name=name)
    db.session.add(ing)

    return ing


def get_recipe_steps(recipe_id: int) -> List[Tuple[int, str]]:
    """ Returns a list of recipe steps (number and methods/directions) by id"""
    steps = []

    for step in RecipeStep.query.filter(RecipeStep.recipe_id == recipe_id):
        steps.append((step.step_num, step.instruction))
        # steps.append(step.__dict__)

    print(steps)
    return steps


def get_recipe_ingredients(recipe_id: int) -> List[Tuple[int, int]]:
    """ Returns a list of recipe ingredients, (recipe_id, ingredient_id) for a given recipe_id"""
    ingredients = []
    for i in RecipeIngredient.query.filter(RecipeIngredient.recipe_id == recipe_id):
        ingredients.append((i.recipe_id, i.ingredient_id))

    print(ingredients)
    return ingredients


def search_title(search_key: str) -> List[Recipe]:
    """ Returns a list of Recipes containing the search key in title/name """
    recipes = Recipe.query.filter(Recipe.title.like(f'%{search_key}%')).all()
    print('**', recipes)

    for r in recipes:
        print('id:', r.id, 'title:', r.title, 'Ingredients:', r.ingredients)

    return recipes


def join_recipes_with_ingredients_table():
    # result = db.session.query(Recipe).join(Ingredient).all()
    # for row in result:
    #     for ing in row.ings:
    #         print(row.id, row.title, ing.id, ing.name)
    result = db.session.execute("select * from recipes inner join ingredients on recipes.id = ingredients.id")
    for row in result:
        print(row)


def main():
    db.drop_all()
    db.create_all()
    insert_recipe('Tasty Pancakes fruit', 4, 100, 15, 'These pancakes are yummy')
    insert_recipe('Fruit Salad', 3, 300, 5, 'Perfecto!')
    # delete_recipe(1)
    recipe = find_recipe(1)
    ing = create_ingredient('Bananas')
    recipe.ingredients = [ing]
    ing = create_ingredient('Grapes')
    recipe.ingredients.append(ing)

    get_recipe_steps(1)
    search_title('fruit')

    ingredients = get_recipe_ingredients(1)
    for i in ingredients:
        print('Recipe 1 - ingredients:', i)

    print('joinng recipes and ingredients tables...')
    join_recipes_with_ingredients_table()

    db.session.commit()

    print('all goood')


# if __name__ == "__main__":
#     main()
