import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')

s1 = "please turn on the light because the room is dark"
s2 = "this bag is very light, so it is easy to carry"
word = "light"


t1 = word_tokenize(s1)
t2 = word_tokenize(s2)


sense1 = lesk(t1, word)
sense2 = lesk(t2, word)

print("Word:", word)

print("\nSentence 1:", s1)
print("Predicted Sense 1:", sense1)
print("Definition:", sense1.definition())

print("\nSentence 2:", s2)
print("Predicted Sense 2:", sense2)
print("Definition:", sense2.definition())
