from collections import Counter

words = []

with open("file1.txt", "r") as file:
    read_content = file.read()
    words = read_content.lower().replace('\n', ' ').replace(',', '').replace(
        '.', '').split(" ")

freq = Counter(words)
words_new = dict(freq)

sorted_words = sorted(words_new.items(),
                                     key=lambda x: x[1],
                                     reverse=True)

sorted_words = dict(sorted_words)
for key, value in sorted_words.items():
    print(key)
