import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
}


def get_url(url):
    list_url = []
    web_data = requests.get(url=url, headers=headers)
    web_data.encoding = 'utf-8'
    soup = BeautifulSoup(web_data.text, 'lxml')
    targets_url = soup.select('a.item-img')

    for each in targets_url:
        list_url.append(each.img.get('alt') + '= ' + each.get('href'))  # a标签下的img标签中的alt，a标签中的href

    return list_url


def download_images(list_url):
    for each_image in list_url:
        image_info = each_image.split('=')
        filename = image_info[0] + '.jpg'
        target_url = image_info[1]
        print(filename, target_url)
    #     web_data = requests.get(target_url, headers=headers)
    #     web_data.encoding = 'utf-8'
    #     soup1 = BeautifulSoup(web_data.text, 'lxml')
    #     images_url = soup1.find_all('div', class_='wr-single-content-list')
    #     soup2 = BeautifulSoup(str(images_url), 'lxml')
    #     images_url = 'http://www.shuaia.net' + soup2.div.img.get('src')
    #     if 'images' not in os.listdir():
    #         os.makedirs('images')
    #     urlretrieve(images_url, filename='images/' + filename)
    #     time.sleep(1)
    # print('下载完成！')


if __name__ == '__main__':
    for num in range(1, 2):
        if num == 1:
            url = 'http://www.shuaia.net/index.html'
        else:
            url = 'http://www.shuaia.net/index_%d.html' % num
        list_url = get_url(url)
        download_images(list_url)
