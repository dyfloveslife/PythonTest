import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}


def get_data(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    links = soup.find_all('img', class_='zoom')
    for link in links:
        url = link['src']
        print(url)


def get_url(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    links = soup.find_all('a', class_='z')
    for link in links:
        url = 'http://gifcc.com/' + link['href']
        get_data(url)


if __name__ == '__main__':
    urls = ['http://gifcc.com/forum-47-{}.html'.format(str(i)) for i in range(1, 4)]
    for url in urls:
        get_url(url)
        time.sleep(1)