fo = open("sgldout.txt", "r", encoding='utf-8')
words = fo.readlines()
fo.close()

sym = "；，。“”： "
DictWords = {}

for ls in words:
    if ls[:-1] not in sym:
        DictWords[ls[:-1]] = DictWords.get(ls[:-1], 0) + 1
        L = list(DictWords.items())
        L.sort(key=lambda s:s[1], reverse=True)

# 将结果写入到文件
fi = open("sgldstatistics.txt", "w", encoding="utf-8")
for i in range(5):
    fi.writelines(L[i][0]+":"+ str(L[i][1]) + "\n")

# 输出结果
for i in range(5):
    print("{}:{}".format(L[i][0], str(L[i][1])))
fi.close()

