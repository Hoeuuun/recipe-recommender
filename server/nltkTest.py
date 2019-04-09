import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "1/4 cup white sugar"

# print(word_tokenize(example_text))
# splits by word (punctuation (,?;') identified as word also)
#
# word_tokens = word_tokenize(example_text)

ingredient_grammar = nltk.CFG.fromstring("""
S -> Object | Quantity Object
Quantity -> CD | CD NN
Object -> JJ NN | NN
""")

def process_content():

    print(sent_tokenize(example_text))

    try:
        for word in word_tokenize(example_text):
            print(word)
            tagged = nltk.pos_tag([word])
            print(tagged)
    except Exception as e:
        print(e)


process_content()
