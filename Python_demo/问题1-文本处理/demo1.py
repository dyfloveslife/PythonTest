fi = open("论语-网络版.txt", "r", encoding="utf-8")
fo = open("论语-提取版.txt", "w")
wflag = False

for line in fi:
    if "【" in line:
        wflag = False
    if "【原文】" in line:
        wflag = True
        continue
    if wflag == True:
        for i in range(0, 25):
            for j in range(0, 25):
                line = line.replace("{}·{}".format(i, j), "**")
        for i in range(0, 10):
            line = line.replace("*{}".format(i), "")
        for i in range(0, 10):
            line = line.replace("{}*".format(i), "")
        line = line.replace("*", "")
        fo.write(line)

fi.close()
fo.close()
