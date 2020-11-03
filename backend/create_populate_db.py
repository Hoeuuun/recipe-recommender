from typing import Dict, List

from backend.app import create_app
from backend.extensions import db
from backend.model import Recipe, RecipeStep, Ingredient
from backend.parse_json import get_data, remove_duplicates


def main():
    app = create_app()

    with app.app_context():
        db.create_all()

        read_from_file_and_write_to_db('../data/allrecipes/data/recipes.json')


def read_from_file_and_write_to_db(filename):
    recipes_original = get_data('../data/allrecipes/data/recipes.json')
    recipes = remove_duplicates(recipes_original)

    return write_to_db(recipes)


def write_to_db(recipes: List[Dict]):
    """
    Gets the data, and after cleaning it, populates
    the db with each recipe inserted as a row
    """
    with db.session.no_autoflush:
        for recipe in recipes:
            # id = recipe['id']
            title = recipe['title']
            rating = int((recipe['rating_stars'] / 5) * 100)
            review_count = int(recipe['review_count'])
            time = recipe['total_time_minutes']
            url = recipe['url']
            image = recipe['photo_url']
            description = recipe['description']

            ingredients = set(recipe['ingredients'])

            instructions = recipe['instructions']

            if image:
                image = "/".join(image.split("/")[-2:])

            recipe = Recipe(title=title,
                            rating=rating,
                            review_count=review_count,
                            time=time,
                            url=url,
                            image=image,
                            description=description)
            db.session.add(recipe)
            db.session.flush()

            for ingredient_name in ingredients:
                ingredient = db.session.query(Ingredient).filter(Ingredient.name == ingredient_name).one_or_none()
                if ingredient is None:
                    ingredient = Ingredient(name=ingredient_name)
                    db.session.add(ingredient)
                recipe.ingredients.append(ingredient)

            for i, instruction in enumerate(instructions):
                step = RecipeStep(stepNumber=i,
                                  instruction=instruction)

                recipe.steps.append(step)

    db.session.commit()


if __name__ == "__main__":
    main()
