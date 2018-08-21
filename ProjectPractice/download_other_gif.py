import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}


def get_url(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    links = soup.find_all('img', class_='img-responsive lazy image_dta')
    for link in links:
        href = link['data-original']
        download_gif(href)


def download_gif(url):
    r = requests.get(url, headers=headers)
    if url.split('.')[-1] == 'gif':
        with open(url.split('/')[-1], 'wb') as file:
            file.write(r.content)


if __name__ == '__main__':
    urls = ['https://www.doutula.com/photo/list/?page={}'.format(str(i)) for i in range(10, 30)]
    num = 10
    for url in urls:
        get_url(url)
        print('第%d页的gif下载完成...' % num)
        num += 1
        time.sleep(2)