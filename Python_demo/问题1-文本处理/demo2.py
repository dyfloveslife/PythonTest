fi = open("论语-提取版.txt", "r")
fo = open("论语-原文.txt", "w")

for line in fi:
    for i in range(1, 23):
        line = line.replace("({})".format(i), "")
    fo.write(line)
fi.close()
fo.close()
