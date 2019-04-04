BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "Recipe" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"title"	TEXT NOT NULL UNIQUE,
	"rating"	INTEGER,
	"time"	INTEGER,
	"image" TEXT,
	"url" TEXT

);

CREATE TABLE IF NOT EXISTS "RecipeIngredients" (
	"recipeId"	INTEGER NOT NULL,
	"ingredientId"	INTEGER NOT NULL,
	"quantity"	INTEGER NOT NULL,
	PRIMARY KEY("ingredientId","recipeId")
);

CREATE TABLE IF NOT EXISTS "Ingredient" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"name"	TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "RecipeSteps" (
	"recipeId"	INTEGER NOT NULL,
	"stepNumber"	INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	PRIMARY KEY("recipeId","stepNumber")
);

CREATE UNIQUE INDEX IF NOT EXISTS "recipe_ingrdients_index" ON "RecipeIngredients" (
	"recipeId"	ASC,
	"ingredientId"	ASC
);

CREATE INDEX IF NOT EXISTS "recipe_index" ON "Recipe" (
	"rating"	ASC,
	"time"	ASC,
	"title"	ASC
);

CREATE INDEX IF NOT EXISTS "ingredient_name" ON "Ingredient" (
	"name"	ASC
);

COMMIT;