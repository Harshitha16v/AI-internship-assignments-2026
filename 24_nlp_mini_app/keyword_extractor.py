from collections import Counter
import string

print("=== NLP Mini App: Keyword Extractor ===")

text = input("\nEnter your text: ").lower()

# remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# split words
words = text.split()

# stopwords
stopwords = ["is", "the", "a", "and", "to", "in", "of", "this", "that", "it"]

# filter words
filtered_words = [word for word in words if word not in stopwords]

# count frequency
word_freq = Counter(filtered_words)

print("\n--- Top Keywords ---")

for word, count in word_freq.most_common(5):
    print(f"{word} → {count}")