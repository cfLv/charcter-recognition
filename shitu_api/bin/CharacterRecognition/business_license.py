#成员：
#电气1901 李锐志 U201911847
#电气1901 吕超凡 U201911852
#电气1901 李卓   U201911857
#电气1901 韩世栋 U201911854
'''
营业执照识别
'''
import os
import base64
import requests
from general import ORC_Images

class Business_License(ORC_Images):
    def __init__(self, IMG, API_KEY, SECRET_KEY, URLS, detect_direction=True, accuracy='normal'):
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY
        self.img = IMG
        self.urls = URLS
        self.detect_direction = detect_direction
        self.accuracy = accuracy

    def postOrcImg(self):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        url = "{}?access_token={}".format(self.urls, self.get_token())
        if os.path.isfile(self.img):
            with open(self.img, 'rb') as img_file:
                imgs = base64.b64encode(img_file.read())
        else:
            return '文件路径不正确'
        data = {'image': imgs, 'detect_direction': self.detect_direction, 'accuracy': self.accuracy}
        result = requests.post(url, headers=header, data=data)
        return result
