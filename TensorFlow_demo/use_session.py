import tensorflow as tf
import numpy
matrix1 = tf.constant([[3, 3]])  # 一行两列
matrix2 = tf.constant([[2],
                       [2]])  # 两行一列
product = tf.matmul(matrix1, matrix2)  # matrix multiply.
# in numpy, np.dot(matrix1, matrix2)

# method 1
# sess = tf.Session()
# result = sess.run(product)
# print(result)
# sess.close()

# method 2
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)