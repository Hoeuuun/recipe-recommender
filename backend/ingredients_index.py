from nltk.tokenize import word_tokenize

"""
Links a word occurring in the list of ingredients to the recipe 
ids where these ingredients may be found.

It's a dictionary of word -> set of recipe ids.
"""


def update_index(index, recipe):
    """
    Updates a given index with a new recipe.
    """
    recipe_id = recipe['id']
    for ingredient in recipe['ingredients']:
        for word in word_tokenize(ingredient):
            # if the word is not yet in the index, put it into index and map it to empty set
            __update_index(index, word, recipe_id)

    for word in word_tokenize(recipe['title']):
        __update_index(index, word, recipe_id)


def __update_index(index, word, recipe_id):
    """
    Internal helper function that updates the index for each word in ingredients and title.
    """
    word = word.lower()
    if word not in index:
        index[word] = set()
    index[word].add(recipe_id)


def search_recipes_by_ingredient_words(index, ingredient_word_list):
    result = None
    for word in ingredient_word_list:
        recipes = index.get(word)
        if recipes:
            print(f'''Got {len(recipes)} recipes for {word}''')
            if result is None:
                result = recipes.intersection()
            result = result.intersection(recipes)
    if result:
        print("Final search count: ",  len(result))
    else:
        print("Didn't find anything")
    return result
