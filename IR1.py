# Importing necessary libraries from NLTK (Natural Language Toolkit)
import nltk
from nltk.corpus import stopwords        # For removing common words like "is", "the", "and"
from nltk.tokenize import word_tokenize  # For breaking text into individual words
from nltk.stem import PorterStemmer       # For reducing words to their root form

# Downloading necessary data files for tokenization and stopwords
nltk.download('punkt')
nltk.download('stopwords')

# Step 1: Input text
text = "Text preprocessing is a crucial step in natural language processing tasks."

# Step 2: Tokenization - split text into words
tokens = word_tokenize(text.lower())   # convert to lowercase and split into tokens
# Example output: ['text', 'preprocessing', 'is', 'a', 'crucial', 'step', 'in', 'natural', 'language', 'processing', 'tasks', '.']

# Step 3: Stop word removal - remove common unimportant words
stop_words = set(stopwords.words('english'))   # list of common stopwords
filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
# word.isalpha() removes punctuation (like '.')
# Example output: ['text', 'preprocessing', 'crucial', 'step', 'natural', 'language', 'processing', 'tasks']

# Step 4: Stemming - reduce words to their root/base form
stemmer = PorterStemmer()   # create stemmer object
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
# Example output: ['text', 'preprocess', 'crucial', 'step', 'natur', 'languag', 'process', 'task']

# Step 5: Print final result
print("Stemmed Tokens:", stemmed_tokens)
