import random

s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
random.seed(0x1010)
ls = []
excludes = ""
while len(ls) < 10: # 每个密码长度固定为 10 个字符
    pwd = ""
    for i in range(10): # 程序运行每次产生 10 个密码，每个密码一行
        pwd += s[random.randint(0, len(s)-1)]
    if pwd[0] in excludes: # 每次产生的 10 个密码首字符不能一样
        continue
    else:
        ls.append(pwd)
        excludes += pwd[0]
print("\n".join(ls))
