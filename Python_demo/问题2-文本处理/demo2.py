import jieba

fi = open("天龙八部-网络版.txt", 'r', encoding="utf-8")
fo = open("天龙八部-词语统计.txt", 'w', encoding="utf-8")
txt = fi.read()
fenci = jieba.lcut(txt)
print(type(fenci))

d = {}
for word in fenci:
    d[word] = d.get(word, 0) + 1

del d[' ']
del d['\n']

ls = []
for key in d:
    ls.append("{}:{}".format(key, d[key]))

fo.write(', '.join(ls))

fi.close()
fo.close()
