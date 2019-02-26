from flask import Flask
from flask import request, jsonify

from app.captcha import KnnCaptcha
import requests
import re
from app.captcha_process import image_process, imsave

app = Flask(__name__)

knn_captcha = KnnCaptcha()

#更新
#base_url = 'http://202.207.247.49'
#base_url = 'http://urp.tyut.risid.com'
#base_url = 'http://wesw7votbh.bjhttp.cn/'
#base_url = 'http://wesw7votbh.bjhttp.cn'
#base_url = 'http://urp.intyut.cn:7889'
#base_url = 'http://202.207.247.44:8089'
base_url = 'http://202.207.247.44:8065/'

@app.route('/', methods=['POST'])
def login_router():
    #captcha_path = request.form['captcha_path']
    #login_path = request.form['login_path']
    captcha_path = base_url+'/validateCodeAction.do?random=0.78756204832' #request.form['captcha_path']
    login_path = base_url + '/loginAction.do' #request.form['login_path']
    token = request.form['token']
    username =  request.form['username']
    password =  request.form['password']

    headers = {
        'Referer': '202.207.247.49',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.133 Safari/537.36',
        'Cookie': 'JSESSIONID=%s' % token
    }

    for i in [1, 2, 3]:
        r = requests.get(url=captcha_path, headers=headers) # 获取验证码
        X_test = image_process(r.content) # 处理验证码

        captcha = knn_captcha.predict(X_test)

        flag, msg = login(login_path, username, password, captcha=captcha, token=token)
        if flag:
            return jsonify({'code': 1, 'msg': '登陆成功', 'data': token})
        elif msg is not None: # 如果返回消息不为空
            return jsonify({'code': -1, 'msg': msg, 'data': None})

        # 到这里说明验证码识别错误
        if flag == False and msg is None:
            imsave(r.content, './captcha/%s-%s.jpg' % (token, captcha))

    return jsonify({'code': -1, 'msg': '服务器正忙,请稍后重试', 'data': None})

def login_handler(text):
    m = re.findall(r'(?=<title>)<title>(.*)(?=</title>)', text, flags=re.M)
    for i in m:
        if i == '学分制综合教务':
            return True, None

    err = re.findall('<font color=\"#990000\">(.*?)</font>', text)

    for i in err:
        if len(i) > 0:
            if i.count('验证码错误') > 0:
                return False, None
            return False, i

    return False, '出现未知错误,请稍后重试'


def login(url,username, password, captcha, token):
    login_params = {
        'zjh': username,
        'mm': password,
        'v_yzm': captcha
    }

    header = {
        'Referer': '202.207.247.49',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Cookie': 'JSESSIONID=%s' % token
    }

    resp = requests.post(url, data=login_params, headers=header)

    if resp.status_code != 200:
        return False, '出现未知错误,请稍后重试'

    return login_handler(resp.text)

# if __name__ == '__main__':
    # m = re_test.match(r'(?=<title>)<title>(.*)(?=</title>)', text, flags=re_test.M)
    # print(m)
    # app.run(port=8080)
