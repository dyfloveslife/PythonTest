# 先统计字符个数，再删除无效字符，
# 再将字符添加到列表中，以便对其用join函数进行分割。

fi = open("天龙八部-网络版.txt", 'r', encoding='utf-8')
fo = open("天龙八部-汉字统计.txt", 'w', encoding='utf-8')
txt = fi.read()
print(type(txt))
'''
d={}
for word in txt:
    d[word] = d.get(word, 0) + 1

del d[" "]
del d["\n"]

ls = []
for key in d:
    ls.append("{}:{}".format(key, d[key]))

fo.write(",".join(ls))
'''
fo.close()
fi.close()
