《天龙八部》是著名作家金庸的代表作之一，历时4年创作完成。该作品气势磅礴，人物众多，非常经典。这里给出一个《天龙八部》的网络版本，文件名为“天龙八部-网络版.txt”。

# 问题1：
请编写程序，对这个《天龙八部》文本中出现的汉字和标点符号进行统计，字符与出现次数之间用冒号:分隔，输出保存到“天龙八部-汉字统计.txt”文件中，该文件要求采用 CSV 格式存储，参考格式如下（注意，不统计空格和回车字符）：
```
天:100, 龙:110, 八:109, 部:10

（略）
```

# 问题2：
请编写程序，对《天龙八部》文本中出现的中文词语进行统计，采用 jieba 库分词，词语与出现次数之间用冒号:分隔，输出保存到“天龙八部-词语统计.txt”文件中。参考格式如下（注意，不统计任何标点符号）：
```
天龙:100, 八部:10

（略）
```