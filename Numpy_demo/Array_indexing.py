import numpy as np

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# b = a[:2, 1:3]  # 注意索引是从0开始的
# print(a)
# print('------')
# print(b)
# print('------')
# print(a[0, 1])
# b[0, 0] = 77
# print(a[0, 1])  # a和b指向同一索引

# row_r1 = a[1, :]
# row_r2 = a[1:2, :]
#
# print(a)
# print('-------------')
# print(row_r1, row_r1.shape)
# print(row_r2, row_r2.shape)
# print('-------------')
# col_r1 = a[:, 1]
# col_r2 = a[:, 1:2]
# print(col_r1, col_r1.shape)
# print(col_r2, col_r2.shape)

# a = np.array([[1, 2], [3, 4], [5, 6]])
# print(a, a.shape)
# print('---------')
# print(a[[0, 1, 2], [0, 1, 0]])
# The above example of integer array indexing is equivalent to this:
# print(np.array([a[0, 0], a[1, 1], a[2, 0]]))
# print('---------')
# print(a[[0, 0], [1, 1]])
# same this:
# print(np.array([a[0, 1], a[0, 1]]))
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print(a)
# b = np.array([0, 2, 0, 1])
# print('-----------')
# print(a[np.arange(4), b])  # 使用b中的索引从a的每一行中选择一个元素
# print('-----------')
# a[np.arange(4), b] += 10  # 使用b中的索引来变换a的每一行中的一个元素
# print(a)

# Boolean array indexing
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)
print('-------')

bool_idx = (a > 2)

print(bool_idx)
print(a[bool_idx])
# same this:
print(a[a > 2])
