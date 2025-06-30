text = open("sample.txt", "r").read()
words = text.split()
num_words = len(words)
num_chars = 0
for w in words:
    num_chars += len(w)
sentences = text.split(".")
num_sentences = len(sentences)
common = {}
for word in words:
    if word in common:
        common[word] += 1
    else:
        common[word] = 1
most_common = ""
count = 0
for word in common:
    if common[word] > count:
        count = common[word]
        most_common = word
print("Words:", num_words)
print("Characters:", num_chars)
print("Sentences:", num_sentences)
print("Most Common Word:", most_common)
print("Average Word Length:", num_chars / num_words)
