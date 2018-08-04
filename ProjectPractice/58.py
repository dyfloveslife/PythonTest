from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}


def get_info():
    url = 'http://zhuanzhuan.58.com/detail/1025195595239473164z.shtml?fullCate=5%2C38484%2C23094&fullLocal=4&from=pc&metric=null&PGTID=0d305a36-0000-4ac2-6da3-b0a01c446a53&ClickID=2'
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select('.info_titile')
    prices = soup.select('.price_now > i')
    regions = soup.select('.palce_li > span > i')
    views = soup.select('.look_time')
    series = soup.select('.crb_i > a')

    total = []
    for title, price, region, view, serie in zip(titles, prices, regions, views, series):
        data = {
            'title': title.get_text(),
            'price': price.get_text(),
            'region': region.get_text(),
            'view': view.get_text(),
            'serie': serie.get_text().strip(),
        }
        total.append(data)
    for i in total:
        print(i)
    with open('58Total.txt', 'a', encoding='utf-8') as file:
        for i in total:
            file.write(str(i) + '\n')

def get_all_items(url):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    hrefs = soup.select('a.t')  # a标签下的class是t，点代表class，> 代表父与子的关系
    for href in hrefs:
        links = href.get('href')
        if 'zhuanzhuan' in links:
            get_info(links)


if __name__ == '__main__':
    urls = ['http://sz.58.com/pbdn/pn{}/'.format(str(i)) for i in range(1, 3)]
    for url in urls:
        with open('58Total.txt', 'a', encoding='utf-8') as dash:
            dash.write('-' * 120 + '\n')
        get_all_items(url)
        print('-' * 120)
        time.sleep(1)
