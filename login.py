"""
__author__: liuyinxin
__time__: 2018/2/1 20:29
"""

import requests


login_params = {
    'zjh': '2016005906',
    'mm': '283617',
    'v_yzm': '1xyd'
}

captcha_url = 'http://127.0.0.1:8080/'

header = {
    'Accept-Encoding' : 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': 'JSESSIONID=bhdGcZdvyo0ayam90Mrfw '
}

token = '3d1d0b28631111e8adc0fa7ae01bbebc'

cap_resp = requests.post(captcha_url, data={
    'token': token,
    'path': 'http://202.207.247.49/validateCodeAction.do?random=0.78756412120483'}
              )

captcha  = cap_resp.json()

login_params['v_yzm'] = captcha['value']
header['COOKIE'] = 'JSESSIONID=' + token

url = "http://202.207.247.49/loginAction.do"

session = requests.Session()

resp = session.post(url, data=login_params, headers=header)
print(resp.text)

class_url = 'http://202.207.247.49/gradeLnAllAction.do?type=ln&oper=qbinfo'

class_resp = session.get(class_url, headers=header)

print(class_resp.text)