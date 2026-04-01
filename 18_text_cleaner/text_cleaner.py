import string
print("=== Smart Text Cleaner ===")
text = input("Enter messy text: ")
print("\nOriginal Text:")
print(text)
text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))
stopwords = ["is", "the", "a", "and", "to", "in", "of", "this", "that"]
words = text.split()
cleaned_words = [word for word in words if word not in stopwords]
cleaned_text = " ".join(cleaned_words)
print("\nCleaned Text:")
print(cleaned_text)