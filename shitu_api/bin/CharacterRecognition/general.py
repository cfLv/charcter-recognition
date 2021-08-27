#成员：
#电气1901 李锐志 U201911847
#电气1901 吕超凡 U201911852
#电气1901 李卓   U201911857
#电气1901 韩世栋 U201911854
'''
百度识图，通用文字识别，网络图片文字识别
'''
import os
import base64
import requests


class ORC_Images(object):

    def __init__(self, IMG, API_KEY, SECRET_KEY, URLS):
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY
        self.img = IMG
        self.urls = URLS

    def get_token(self):
        '''
        获取access_token
        :param API_KEY:
        :param SECRET_KEY:
        :return:
        '''
        access_token_url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=bYg7ytFQ4TzNZeCtGxSfD9YZ&client_secret=WsyFEorSdds1a4MHcUjU43HlidmIje7d".format(
            self.API_KEY, self.SECRET_KEY)
        access_token = requests.post(access_token_url)
        return access_token.json()['access_token']

    def postOrcImg(self):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        url = "{}?access_token={}".format(self.urls, self.get_token())
        if os.path.isfile(self.img):
            with open(self.img, 'rb') as img_file:
                imgs = base64.b64encode(img_file.read())
            data = {'image': imgs}
        else:
            data = {'url': self.img}
        result = requests.post(url, headers=header, data=data)
        return result
