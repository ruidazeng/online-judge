import sys
words = list()
for line in sys.stdin:
    words.extend(line.split())

# unique words
words_set = set(map(lambda x: x.lower(), words))

for word in words:
    if word.lower() in words_set:
        print(word, end = ' ')
        words_set.remove(word.lower())
    else:
        print('.', end = ' ')
print()