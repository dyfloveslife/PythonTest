from collections import Counter
import re

path = 'sample.txt'
file = open(path)
content = file.read()
#  '\w+' 表示正则表达式，匹配单词、数字字符
# 找出content中所有符合正则表达式的字符
words = re.findall('\w+', content)
# Counter是一个简单的计数器，是dict的子类
a = Counter(words)
# most_common(n) 方法返回出现频率最高的n个字符及其计数，顺序为最常见到最少
b = a.most_common(5)
file.close()
print(b)

# 简写
# path = 'sample.txt'
# words = re.findall('\w+', open(path).read())
# print(Counter(words).most_common(5))
