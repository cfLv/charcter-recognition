#成员：
#电气1901 李锐志 U201911847
#电气1901 吕超凡 U201911852
#电气1901 李卓   U201911857
#电气1901 韩世栋 U201911854
#%%
from config import *
from url import *
#%%
from general import ORC_Images
from idcard import Idcard
from banckard import Banckard
from business_license import Business_License
import time
#%%
if __name__ == "__main__":
    # 测试通用文字识别，本地真实图片
    test_orc1 = ORC_Images(IMG='../../testimg/panting.jpg', URLS=GENERAL_URL, API_KEY=GENERAL_API_KEY, SECRET_KEY=GENERAL_SECRET_KEY)
    result1 = test_orc1.postOrcImg()
    print('通用文字识别本地：', result1.json())
#%%
    # 测试通用文字识别（含位置信息版），本地真实图片
    test_orc1 = ORC_Images(IMG='../../testimg/panting.jpg', URLS=GENERAL_High_URL, API_KEY=GENERAL_API_KEY,
                           SECRET_KEY=GENERAL_SECRET_KEY)
    result1 = test_orc1.postOrcImg()
    print('通用文字识别（含位置信息版）本地：', result1.json())

#%%
    # 通用文字识别（高精度含位置版），本地真实图片
    test_orc1 = ORC_Images(IMG='../../testimg/panting.jpg', URLS=GENERAL_ACCURATE_BASIC_URL, API_KEY=GENERAL_API_KEY,
                           SECRET_KEY=GENERAL_SECRET_KEY)
    result1 = test_orc1.postOrcImg()
    print('通用文字识别（高精度含位置版）本地：', result1.json())

#%%
    # 网络图片文字识别，url图片
    test_orc = ORC_Images(IMG='https://www.baidu.com/img/bd_logo1.png?where=super', URLS=WEB_IMAGES_URL,
                          API_KEY=GENERAL_API_KEY, SECRET_KEY=GENERAL_SECRET_KEY)
    result = test_orc.postOrcImg()
    print('weburl: ', result.json())
#%%
    # 数字识别，图片
    from number import Number

    test = Number(IMG='../../testimg/number.jpeg', URLS=NUMBER_URL, API_KEY=GENERAL_API_KEY,
                  SECRET_KEY=GENERAL_SECRET_KEY)
    result = test.postOrcImg()
    print('数字识别：', result.json())
#%%
    # 手写文字识别
    from handwriting import Handwriting

    test = Handwriting(IMG='../../testimg/2.png', URLS=HANDWRITING_URL, API_KEY=GENERAL_API_KEY, SECRET_KEY=GENERAL_SECRET_KEY)
    result = test.postOrcImg()
    print('手写文字识别：', result.json())
#%%
    # 身份证识别，本地真实图片
    test_id = Idcard(IMG='../../testimg/sfz.jpeg', URLS=IDCARD_URL, API_KEY=GENERAL_API_KEY,
                     SECRET_KEY=GENERAL_SECRET_KEY)
    result = test_id.postOrcImg()
    print('身份证：', result.json())
#%%
    # 银行卡识别，本地真实图片
    test_id = Banckard(IMG='../../testimg/yhk.jpeg', URLS=BANCKARD_URL, API_KEY=GENERAL_API_KEY,
                       SECRET_KEY=GENERAL_SECRET_KEY)
    result = test_id.postOrcImg()
    print('银行卡：', result.json())
#%%
    # 营业执照识别，测试
    test = Business_License(IMG='../../testimg/yyzz.jpeg', URLS=BUSINESS_LICENSE_URL, API_KEY=GENERAL_API_KEY,
                            SECRET_KEY=GENERAL_SECRET_KEY)
    result = test.postOrcImg()
    print('营业执照识别：', result.json())

# %%
