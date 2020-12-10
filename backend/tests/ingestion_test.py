import json

from backend.create_populate_db import write_to_db
from backend.parse_json import remove_duplicates
from backend.extensions import db

from backend.model import Recipe, Ingredient, RecipeStep


def test_import_json_data_into_db(app):
    # Given: A JSON object
    json_object = """
    {
   "author":"Stephanie",
   "cook_time_minutes":25,
   "description":"I just started adding my favorite things to basic cornbread and I came up with something great!",
   "error":false,
   "footnotes":[
      
   ],
   "ingredients":[
      "1/2 cup unsalted butter, chilled and cubed",
      "1 cup chopped onion",
      "1 3/4 cups cornmeal",
      "1 1/4 cups all-purpose flour",
      "1/4 cup white sugar",
      "1 tablespoon baking powder",
      "1 1/2 teaspoons salt",
      "1/2 teaspoon baking soda",
      "1 1/2 cups buttermilk",
      "3 eggs",
      "1 1/2 cups shredded pepperjack cheese",
      "1 1/3 cups frozen corn kernels, thawed and drained",
      "2 ounces roasted marinated red bell peppers, drained and chopped",
      "1/2 cup chopped fresh basil"
   ],
   "instructions":[
      "Preheat oven to 400 degrees F (205 degrees C). Butter a 9x9x2 inch baking pan.",
      "Melt 1 tablespoon butter in medium nonstick skillet over medium-low heat. Add onion and saute until tender, about 10 minutes. Cool.",
      "Mix cornmeal with the flour, baking powder, sugar, salt, and baking soda in large bowl. Add 7 tablespoons butter and rub with fingertips until mixture resembles coarse meal.",
      "Whisk buttermilk and eggs in medium bowl to blend. Add buttermilk mixture to dry ingredients and stir until blended. Mix in cheese, corn, red peppers, basil, and onion. Transfer to prepared pan.",
      "Bake cornbread until golden and tester inserted comes out clean, about 45 minutes. Cool 20 minutes in pan. Cut cornbread into squares."
   ],
   "photo_url":"http://images.media-allrecipes.com/userphotos/560x315/582853.jpg",
   "prep_time_minutes":55,
   "rating_stars":4.32,
   "review_count":46,
   "time_scraped":1498204021,
   "title":"Basil, Roasted Peppers and Monterey Jack Cornbread",
   "total_time_minutes":100,
   "url":"http://allrecipes.com/Recipe/6664/"
}
                """

    # When: We load this object into our SQLite DB
    with app.app_context():
        write_to_db([json.loads(json_object)])
        db.session.commit()

        # Then: The object will be inserted as a new recipe row
        rows = db.session.query(Recipe).count()
        assert rows == 1

        # Then: The Ingredients table will contain a list of ingredient IDs and names for the recipe
        ingredient_list = db.session.query(Ingredient).count()
        assert ingredient_list == 14

        # Then The RecipeStep table will contain a list of steps for the given recipe
        recipe_steps = db.session.query(RecipeStep).count()
        assert recipe_steps == 5


def test_parse_json(app):
    # Given: A list with two JSON objects with the same titles and descriptions
    recipes = [{"title":"Basil, Roasted Peppers and Monterey Jack Cornbread",
                "description":"I came up with something great!"},
               {"title":"Basil, Roasted Peppers and Monterey Jack Cornbread",
                "description":"I came up with something great!"}]
    # When: We call our remove_duplicates function, passing in this list
    unique_recipe_list = remove_duplicates(recipes)

    # Then: The list should contain only one JSON object
    assert len(unique_recipe_list) == 1

