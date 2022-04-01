from urllib import parse
import os,json,requests
from jsonpath import jsonpath
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

report = os.path.join(path, 'allure-report')
tpath = os.path.join(path, 'weathers/')



def weather():
    url = "https://v2-zhwnlapi.etouch.cn"
    path = "/Ecalender/api/sign/weather"
    result_url = parse.urljoin(url, path)
    payload = {
        "app_key": 99817882,
        "citykey": 101010300,
        "date": 20211012,
        "pic_ver": 2
    }
    res = requests.get(url=result_url, params=payload, verify=False)
    data = res.json()

    result = ("明天日期：%s" % jsonpath(data, '$..date')[2] + '\n' +
              "明天天气：%s" % jsonpath(data, '$..day.wthr')[2] + '\n' +
              "空气质量：%s" % jsonpath(data, '$..aqi_level_name')[2] + '\n' +
              "最高气温：%s度" % jsonpath(data, '$..high')[2] + '\n' +
              "最低气温：%s度" % jsonpath(data, '$..low')[2] + '\n' +
              "每日祝福：%s" % jsonpath(data, '$..day.notice')[2])
    return result


# def test_sendemail():
#     yag = yagmail.SMTP(user="825664936@qq.com", password='chjcwbaalukrbajg', host='smtp.qq.com')
#
#     yag.send("18519109588@163.com", "每日天气", contents=test_weather())
#     print('邮件已发送')

def sendwx():
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f75dba7b-cf03-4f1e-b9ab-913e5ace4ff2"  # 大
    # url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=7c978e36-fcc2-476d-9dc0-9e0950712865"    #小

    payload = json.dumps({
        "msgtype": "news",
        "news": {
            "articles": [
                {
                    "title": "测试组天气预告温馨提醒",
                    "description": weather(),
                    "url": "https://m.baidu.com/from=1000539d/pu=sz%401320_2001/s?word=天气预报&sa=ts_1&ts=8685821&t_kt=0&ie=utf-8&rsv_t=f71eemDBqof0rt7Fa9JzPJ97NW0r1J4K8RPx11s%252BXexDasQWqL786mZoO6Vt3Hk&rsv_pq=12752381271097209776&ss=100&sugid=219256368111660&rq=ti%E2%80%86a&rqlang=zh&rsv_sug4=3929&inputT=1942&oq=日历",
                    "picurl": 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn.sinaimg.cn%2Fsinakd20220222s%2F302%2Fw640h462%2F20220222%2F4f21-34a1fdd554599a0bfd9397dd542290eb.jpg&refer=http%3A%2F%2Fn.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1651231129&t=c7eed4e941953a3a1396f8a9554b334f'
                }
            ]
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    print(response.text)


if __name__ == '__main__':
    weather()
