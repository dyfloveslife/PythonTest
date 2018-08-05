import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
}


def get_data(url):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')

    titles = soup.select('h3.name')
    styles = soup.select('li.ellipsis')
    directors = soup.select('div.info > a.name')

    title = titles[0].get_text()
    style = styles[0].get_text()
    country = styles[1].get_text().strip().split()[0]
    time = styles[1].get_text().strip().split()[2]
    director = directors[0].get_text().strip()
    data = {
        'title': title,
        'style': style,
        'country': country,
        'time': time,
        'director': director,
    }
    print(data)


def get_all_items(url):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    href = soup.select('p.name > a')
    for href in href:
        get_data('http://maoyan.com' + href.get('href'))


if __name__ == '__main__':
    urls = ['http://maoyan.com/board/4?offset={}'.format(str(i)) for i in range(0, 100, 10)]
    for url in urls:
        get_all_items(url)
        print('-' * 100)
