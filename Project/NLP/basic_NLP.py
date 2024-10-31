import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np
stemer = PorterStemmer()
def tokenize(sentence):
    return nltk.word_tokenize(sentence)
def stem(word):
    return stemer.stem(word.lower())
def bag_of_words(tokenize_sentence, all_words):
    tokenize_sentence = [stem(word) for word in tokenize_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenize_sentence:
            bag[idx] = 1.0
    return bag

a = "How are you?"
print(a)
print("Tokenize :",tokenize(a))

b = ['Organize', 'Organizes', 'Organizing']
bb = [stem(word) for word in b]
print(b)
print("Stem :",bb)

sentence = ["hello", "how", "are", "you"]
words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
bog = bag_of_words(sentence, words)
print("bog :",bog)