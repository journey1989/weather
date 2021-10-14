import requests
from urllib import parse
import yagmail, json, pytest
import allure
import os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


report = os.path.join(path, 'allure-report')

@allure.feature('天气接口')
def test_weather():
    url = "https://v2-zhwnlapi.etouch.cn"
    path = "/Ecalender/api/sign/weather"
    result_url = parse.urljoin(url, path)
    payload = {
        "app_key": 99817882,
        "citykey": 101010300,
        "date": 20211012,
        "pic_ver": 2
    }
    res = requests.get(url=result_url, params=payload)
    data = res.json()

    return json.dumps(("今天日期: %s" % data['forecast'][1].get("date"))).encode('utf-8').decode('unicode_escape'), \
           json.dumps(("今天天气： %s" % data['forecast'][1].get("day").get("wthr"))).encode('utf-8').decode(
               'unicode_escape'), \
           json.dumps(("空气质量： %s" % data['forecast'][1].get("aqi_level_name"))).encode('utf-8').decode(
               'unicode_escape'), \
           json.dumps(("最高气温： %s度" % data['forecast'][1].get("high"))).encode('utf-8').decode('unicode_escape'), \
           json.dumps(("最低气温： %s度" % data['forecast'][1].get("low"))).encode('utf-8').decode('unicode_escape'), \
           json.dumps(("每日祝福语：%s" % data['forecast'][1].get("day").get("notice"))).encode('utf-8').decode(
               'unicode_escape')


def test_sendemail():
    yag = yagmail.SMTP(user="825664936@qq.com", password='chjcwbaalukrbajg', host='smtp.qq.com')

    yag.send("lilei@yixia.com", "每日天气", contents=test_weather())
    print('邮件已发送')


if __name__ == '__main__':
    pytest.main(["-v", "-s", "weather/weathers","--alluredir=%s"%report])