fi = open("SunSign.csv", "r", encoding="utf-8")
ls = []
for line in fi:
    line = line.replace("\n", "")
    ls.append(line.split(","))
print(ls)
print("---"*20)
fi.close()


while True:
    inputStr = input("请输入星座名称(exit退出):")
    flag = False
    if inputStr == "exit":
        break
    for line in ls:
        if inputStr == line[0]:
            #print("{}的生日位于{}-{}之间".format(inputStr, line[1], line[2]))
            print("{}的生日位于{}-{}之间".format(chr(eval(line[3])), line[1], line[2]))
            flag = True
    if flag == False:
        print("输入星座名称有误！")
