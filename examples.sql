SELECT *
FROM Recipe
WHERE id in
      (SELECT recipeId from RecipeIngredients where ingredientId = (SELECT id from Ingredient where name = "3 eggs"))


DROP VIEW view_recipes_with_first_ing;
DROP VIEW view_recipes_with_second_ing;
DROP VIEW view_recipes_with_third_ing;
DROP VIEW view_recipes_with_fourth_ing;
DROP VIEW view_recipes_with_fifth_ing;
DROP VIEW view_recipes_with_sixth_ing;


CREATE VIEW view_recipes_with_first_ing AS
SELECT * FROM Recipe
                    JOIN RecipeIngredients
                         ON RecipeIngredients.recipeId=Recipe.id
                    JOIN Ingredient
                         ON Ingredient.id= RecipeIngredients.ingredientId
WHERE Ingredient.name LIKE '%flour%'
GROUP BY Recipe.id;

SELECT * FROM view_recipes_with_first_ing;

CREATE VIEW view_recipes_with_second_ing AS
SELECT * FROM view_recipes_with_first_ing FI
                    JOIN RecipeIngredients
                         ON RecipeIngredients.recipeId=FI.id
                    JOIN Ingredient
                         ON Ingredient.id= RecipeIngredients.ingredientId
WHERE Ingredient.name LIKE '%sugar%'
GROUP BY FI.id;

SELECT * FROM view_recipes_with_second_ing;

CREATE VIEW view_recipes_with_third_ing AS
SELECT * FROM view_recipes_with_second_ing SI
                    JOIN RecipeIngredients
                         ON RecipeIngredients.recipeId=SI.id
                    JOIN Ingredient
                         ON Ingredient.id= RecipeIngredients.ingredientId
WHERE Ingredient.name LIKE '%basil%'
GROUP BY SI.id;

SELECT * FROM view_recipes_with_third_ing;

CREATE VIEW view_recipes_with_fourth_ing AS
SELECT * FROM view_recipes_with_third_ing TI
                    JOIN RecipeIngredients
                         ON RecipeIngredients.recipeId=TI.id
                    JOIN Ingredient
                         ON Ingredient.id= RecipeIngredients.ingredientId
WHERE Ingredient.name LIKE '%baking soda%'
GROUP BY TI.id;

SELECT * FROM view_recipes_with_fourth_ing;

CREATE VIEW view_recipes_with_fifth_ing AS
SELECT * FROM view_recipes_with_fourth_ing FI
                    JOIN RecipeIngredients
                         ON RecipeIngredients.recipeId=FI.id
                    JOIN Ingredient
                         ON Ingredient.id= RecipeIngredients.ingredientId
WHERE Ingredient.name LIKE '%cornmeal%'
GROUP BY FI.id;

SELECT * FROM view_recipes_with_fifth_ing;

CREATE VIEW view_recipes_with_sixth_ing AS
SELECT * FROM view_recipes_with_fifth_ing FFI
                    JOIN RecipeIngredients
                         ON RecipeIngredients.recipeId=FFI.id
                    JOIN Ingredient
                         ON Ingredient.id= RecipeIngredients.ingredientId
WHERE Ingredient.name LIKE '%pepperjack cheese%'
GROUP BY FFI.id;

SELECT * FROM view_recipes_with_sixth_ing;

