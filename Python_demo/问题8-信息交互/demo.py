menu = ["1. 显示所有信息", "2. 追加信息", "3. 删除信息"]
flag = True
while flag:
    for m in menu:
        print(m)
    try:
        ch = int(input("请输入数字1-3选择功能："))
        flag = False
    except:
        flag = True
    if ch < 1 or ch > 3:
        flag = True
print("您选择了功能", ch)


def display():
    fo1 = open("address.txt", "r", encoding="utf-8")
    for line in fo1.readlines():
        line = line.replace("\n", "")
        print(line)
    fo1.close()


def insertrec():
    fi = open("address.txt", 'r')
    fo = open("new_address.txt", 'w')
    la = []
    for l in fi:
        la.append(l.replace("\n", ""))
    rec = input("请输入要插入的信息，以逗号隔开：")
    la.append(rec)
    for l in la:
        fo.write(l)
        fo.write("\n")
    for i in la:
        print(i)
    fi.close()
    fo.close()


if ch == 1:
    display()
elif ch == 2:
    insertrec()
elif ch == 3:
    pass
