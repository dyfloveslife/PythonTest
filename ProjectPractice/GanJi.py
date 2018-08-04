from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}


def get_data(url):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select('.card-title > i')
    prices = soup.select('.price')
    house_types = soup.select('li.item.f-fl > span.content')
    series = soup.select('div.f-crumbs.f-w1190')

    for title, price, house_type, series in zip(titles, prices, house_types, series):
        data = {
            'title': title.get_text(),
            'price': price.get_text() + '万',
            'house_type': house_type.get_text(),
            'serie': series.get_text().split()[6],
        }
        print(data)


def get_all_items(url):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    hrefs = soup.select('.dd-item.title > a')
    for href in hrefs:
        links = href.get('href')
        if 'fang5' in links:
            get_data('http://linyi.ganji.com' + links)  # 由于返回的不是完成的网站，所以这里需要拼接

if __name__ == '__main__':
    urls = ['http://linyi.ganji.com/fang5/o{}/'.format(str(i)) for i in range(1, 5)]  # 控制访问页数
    for url in urls:
        get_all_items(url)
        print('-' * 120)
