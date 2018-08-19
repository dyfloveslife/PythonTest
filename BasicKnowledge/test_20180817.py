import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup

# plyload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r = requests.post('http://httpbin.org/post', data=plyload)
#
# print(r.text)

# url = 'http://httpbin.org/post'
# files = {'file': open('example.log', 'rb')}
#
# r = requests.post(url, files=files)
# print(r.text)

# url = 'https://www.baidu.com'
# r = requests.get(url)
# # print(r.raise_for_status())
# print(r.headers)
# print(r.headers['Cache-Control'])

# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working', abc='123')
# r = requests.get(url, cookies=cookies)
#
# print(r.text)


# r = requests.get('http://github.com', allow_redirects=False)
# print(r.status_code)

# r = requests.get('https://api.github.com/repos/requests/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
# if (r.status_code == requests.codes.ok):
#     print(r.headers['content-type'])
#
# commit_data = r.json()
# print(commit_data.keys())
# print(commit_data[u'committer'])
# print(commit_data[u'message'])

html_doc = """
<html><head><title>The Dormouse's story_1</title></head>
<body>
<p class="title"><b>The Dormouse's story_2</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# soup = BeautifulSoup(html_doc, 'lxml')
# print(soup.prettify())
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find(id='link2'))
# for link in soup.find_all('a'):
#     print(link.get('href'))
# print(soup.get_text())
# css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'lxml')
# print(css_soup.name)
# markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
# soup = BeautifulSoup(markup, 'lxml')
# comment = soup.b.string
# print(comment)
soup = BeautifulSoup(html_doc, 'lxml')
# print(soup.title)
# print(soup.body.b)
# links = soup.find_all('a')
# print(links)
# print(soup.find_all(['a', 'b']))
# print(soup.find_all('p', 'title'))
# print(soup.find_all(attrs={'data-foo':'value'}))
print(soup.find_all('a', class_='sister'))