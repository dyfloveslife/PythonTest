lst = [1, 2, 3, 4, 5]
with open('test.txt', 'w') as file:
    file.writelines(lst)