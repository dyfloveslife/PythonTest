import jieba
with open("sgld.txt","r",encoding ="utf-8")as f:
    lssgld = f.readlines()
n = 0
for ls in lssgld:
    ls = ls.strip()
    wordlist = list(jieba.cut(ls))
    if "人" in wordlist:
        n += 1
print("人:" + str(n) + "次")
