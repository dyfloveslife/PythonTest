import time

import requests
from bs4 import BeautifulSoup

# from pymongo import MongoClient

# client - MongoClient()
# songs = client.kugou_db.songs

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}


def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # 在写CSS时，标签名不加任何修饰，类名前加点，id名前加  # ，在这里我们也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list
    ranks = soup.select('.pc_temp_num')
    titles = soup.select('.pc_temp_songlist > ul > li > a')  # 查找字标签
    song_times = soup.select('.pc_temp_time')
    # select 方法返回的结果都是列表形式，可以遍历形式输出，然后用 get_text() 方法来获取它的内容。
    for rank, title, song_time in zip(ranks, titles, song_times):
        data = {
            'rank': rank.get_text().strip(),
            'singer': title.get_text().split('-')[0].strip(),
            'song': title.get_text().split('-')[1].strip(),
            'time': song_time.get_text().strip(),
        }
        print(data)
        # song_id = songs.insert(data)  # insert database
        # print(song_id)



if __name__ == '__main__':
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1, 2)]
    for url in urls:
        get_info(url)
        time.sleep(5)
