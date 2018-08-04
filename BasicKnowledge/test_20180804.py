# a = [i ** 2 for i in range(1, 10)]
# k = [n for n in range(1, 10) if n % 2 == 0]
# z = [letter.lower() for letter in 'ABCD']
# d = {i: i + 1 for i in range(4)}
# g1 = {i: j for i, j in zip(range(1, 6), 'abcde')}
# g2 = {i: j.upper() for i, j in zip(range(1, 6), 'abcde')}
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# for num, letter in enumerate(letters):
#     print(letter, num + 1)

# print(a)
# print(k)
# print(z)
# print(d)
# print(g1)
# print(g2)

# lyric = 'The night begin to shine, the night begin to shine'
# words = lyric.split()
# print(words)
import string

path = 'Walden.txt'
with open(path, 'r', encoding='UTF-8') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    counts_dict = {index: words.count(index) for index in words_index}

for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
    print('{} -- {} times'.format(word, counts_dict[word]))
