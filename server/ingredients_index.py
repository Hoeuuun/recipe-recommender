from nltk.tokenize import sent_tokenize, word_tokenize

"""
Ingredients word index links a word occuring in ingredients to recipe 
ids where these ingredients may be found.

It's a dictionary of word -> set of recipe ids.
"""

def update_index(index, recipe):
    """
    Update given index with a new recipe.
    """
    for ingredient in recipe['ingredients']:
        for word in word_tokenize(ingredient):
            # if word is not yet in index, put it into index and
            # map it to empty set
            if not word in index:
                index[word] = set()
            index[word].add(recipe['id'])


def search_recipes_by_ingredient_words(index, ingredient_word_list):
    result = None
    for word in ingredient_word_list:
        recipes = index.get(word)
        if recipes:
            print("Got %d recipes for %s" % (len(recipes), word))
            if result is None:
                result = recipes.intersection()
            result = result.intersection(recipes)
    return result
