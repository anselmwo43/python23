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

# word frequency
# the the the text analyzer
# word_frequency = {"the": 3, "text": 1, "analyzer": 1}
word_frequency = {}
words_lc = [word.lower() for word in words]
print(words_lc)
for word in unique_words:
    word_frequency[word] = words_lc.count(word)

print(f"The frequency of the words were: {word_frequency}")