# input
word = input("Type in the text to be analyzed: ")
words = word.split()

# word count
word_count = len(words)
print(f"Your text is {word_count} word(s) long.")

# unique words
unique_words = set()
for word in words:
    unique_words.add(word.lower())

print(f"Your text has {len(unique_words)} unique word(s).\nThe word(s) is/are: ")
for word in unique_words:
    print(word)