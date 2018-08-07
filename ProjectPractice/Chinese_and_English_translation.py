import json

import requests


def translate(word):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    if response.status_code == 200:
        return response.text
    else:
        print("有道词典调用失败")
        return None


def get_reuslt(repsonse):
    # 通过 json.loads 把返回的结果加载成 json 格式
    result = json.loads(repsonse)
    print("翻译结果为：%s" % result['translateResult'][0][0]['tgt'])

def main():
    status = True
    while status:
        word = input('请在下面输入你想要翻译的词或句，输入\'exit()\'退出本程序：\n')
        if word == 'exit()':
            status = False
            print('已退出！')
        else:
            list_trans = translate(word)
            get_reuslt(list_trans)

if __name__ == '__main__':
    main()
