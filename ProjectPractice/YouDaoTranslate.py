import json
import requests


def translate(words):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    key = {
        'i': words,
        'from': 'AUTO',
        'smartresult': 'AUTO',
        'client': 'fanyideskweb',
        'salt': '1533608683933',
        'sign': 'd853b83ca70a5716709e85e4a882ea48',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
    }
    response = requests.post(url, data=key)
    if response.status_code == 200:
        return response.text
    else:
        return print('The youdao dictionary call failed！')


def get_result(response):
    # 将返回结果的JSON格式字符串解码（decoding）成Python对象
    result = json.loads(response)
    print('Results:%s' % result['translateResult'][0][0]['tgt'])


if __name__ == '__main__':
    status = True
    while status:
        words = input('Please enter words or sentences, Enter exit() to exit the program:\n')
        if words == 'exit()':
            status = False
            print('Exited!')
        else:
            response = translate(words)
            get_result(response)
