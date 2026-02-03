
from nltk.corpus import stopwords
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer, RegexpStemmer

text = """the product quality is very good and I am extremely happy with the service.
The delivery was late, but the customer support was helpful.
Overall, the experience was positive and I would recommend this company."""

words = [
    w for w in word_tokenize(text.lower())
    if w.isalpha() and w not in stopwords.words('english')
]

print("Words after stop words removal\n", words)

porter = PorterStemmer()
snowball = SnowballStemmer("english")
lancaster = LancasterStemmer()
regex = RegexpStemmer('ing$|ed$|ly$|es$|')

print("\nPorter Stemmer:", [porter.stem(w) for w in words])
print("\nSnowball Stemmer:", [snowball.stem(w) for w in words])
print("\nLancaster Stemmer:", [lancaster.stem(w) for w in words])
print("\nRegex Stemmer:", [regex.stem(w) for w in words])

