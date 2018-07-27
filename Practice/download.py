import os
import requests


def download(url):
    '''
    从指定的 URL 中下载文件并存储到当前目录
    :param url: 要下载的文件的 URL
    '''
    r = requests.get(url)
    if r.status_code == 404:  # 判断网站中的文件是否存在
        print('No such file at %s' % url)
        return
    filename = url.split('/')[-1]
    if os.path.isfile(filename):  # 若sample.txt文件存在，则输出提示
        print('Existed file: %s' % filename)
    else:
        with open(filename, 'wb') as file:
            file.write(r.content)
            print('Download over!')


if __name__ == '__main__':
    url = 'http://labfile.oss.aliyuncs.com/courses/596/sample.txt'
    download(url)
