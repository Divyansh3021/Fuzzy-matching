from fuzzywuzzy import fuzz, process
import random
import string
import nltk
import time

# Download the English word corpus
nltk.download('words')

# Get the list of English words
english_words = nltk.corpus.words.words()

# Generate a list of 10,000 entries with random English words
entries = random.choices(english_words, k=10000)

# Sample keyword to search
keyword = "apple"

start = time.time()
# Partial Matching Example
partial_matches = [doc for doc in entries if keyword in doc]

partial = time.time()
# Fuzzy Search Example
fuzzy_results = process.extract(keyword, entries, scorer=fuzz.ratio, limit=3)
# print("Fuzzy Search Results:", fuzzy_results)

end = time.time()
print("Partial Matches: ",partial_matches)
print("Run time: ", partial-start)
print("\n\n\n")
print("Fuzzy Matches:", fuzzy_results)
print("Run time: ", end-partial)

