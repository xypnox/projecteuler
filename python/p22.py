f = open("p022_names.txt")
values = {chr(i): i - 64 for i in range(ord("A"), ord("A") + 26)}
k = 0
for l in f:
    ln = l
    k += 1
words_raw = l.split(',')
words = []
for word in words_raw:
    words.append(word.strip('\"'))

words.sort()
index = 1
total = 0
for word in words:
    word_point = 0
    for letter in word:
        word_point += values[letter]
    word_point *= index
    index += 1
    total += word_point

print(values, total)
