import requests
from urllib import parse
import yagmail, json, pytest
import allure
import os,random

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


report = os.path.join(path, 'allure-report')
tpath = os.path.join(path, 'weathers/')

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
    res = requests.get(url=result_url, params=payload, verify=False)
    data = res.json()


    result = json.dumps(("明天日期: %s" % data['forecast'][2].get("date"))).encode('utf-8').decode('unicode_escape') +'\n'+ json.dumps(("明天天气： %s" % data['forecast'][2].get("day").get("wthr"))).encode('utf-8').decode(
               'unicode_escape') +'\n'+ json.dumps(("空气质量： %s" % data['forecast'][1].get("aqi_level_name"))).encode('utf-8').decode(
               'unicode_escape') +'\n'+  json.dumps(("最高气温： %s度" % data['forecast'][1].get("high"))).encode('utf-8').decode('unicode_escape') +'\n'+ json.dumps(("最低气温： %s度" % data['forecast'][1].get("low"))).encode('utf-8').decode('unicode_escape') +'\n'+ json.dumps(("每日祝福：%s" % data['forecast'][1].get("day").get("notice"))).encode('utf-8').decode(
               'unicode_escape')
    sendwx(result)
    # return json.dumps(("明天日期: %s" % data['forecast'][2].get("date"))).encode('utf-8').decode('unicode_escape'), \
    #        json.dumps(("明天天气： %s" % data['forecast'][2].get("day").get("wthr"))).encode('utf-8').decode(
    #            'unicode_escape'), \
    #        json.dumps(("空气质量： %s" % data['forecast'][1].get("aqi_level_name"))).encode('utf-8').decode(
    #            'unicode_escape'), \
    #        json.dumps(("最高气温： %s度" % data['forecast'][1].get("high"))).encode('utf-8').decode('unicode_escape'), \
    #        json.dumps(("最低气温： %s度" % data['forecast'][1].get("low"))).encode('utf-8').decode('unicode_escape'), \
    #        json.dumps(("每日祝福语：%s" % data['forecast'][1].get("day").get("notice"))).encode('utf-8').decode(
    #            'unicode_escape')


# def test_sendemail():
#     yag = yagmail.SMTP(user="825664936@qq.com", password='chjcwbaalukrbajg', host='smtp.qq.com')
#
#     yag.send("18519109588@163.com", "每日天气", contents=test_weather())
#     print('邮件已发送')

def sendwx(result):
    picurl = ['https://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=%E5%A4%A9%E6%B0%94%E9%A2%84%E5%91%8A&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined&cs=4011126730,3208427564&os=1068928139,2054379317&simid=4011126730,3208427564&pn=3&rn=1&di=7060663421343105025&ln=1882&fr=&fmq=1648541792956_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=15&spn=0&pi=0&gsm=0&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Finews.gtimg.com%252Fnewsapp_bt%252F0%252F13745733180%252F641.jpg%26refer%3Dhttp%253A%252F%252Finews.gtimg.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1651133792%26t%3Dc3219470852d34b9b6d905dcb6c77fed&rpstart=0&rpnum=0&adpicid=0&nojc=undefined&dyTabStr=MCwxLDIsMyw2LDQsNSw4LDcsOQ%3D%3D','https://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=%E5%A4%A9%E6%B0%94%E9%A2%84%E5%91%8A&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined&cs=62132575,3203655593&os=1122747204,4194965211&simid=4293052666,770807117&pn=46&rn=1&di=7060663421280190465&ln=1882&fr=&fmq=1648541792956_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=0&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fbkimg.cdn.bcebos.com%252Fpic%252Fc9fcc3cec3fdfc037c930614da3f8794a5c226b7%26refer%3Dhttp%253A%252F%252Fbkimg.cdn.bcebos.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1651133793%26t%3De9df33e8bc4e6d88e3c8d910f0a90b8e&rpstart=0&rpnum=0&adpicid=0&nojc=undefined&dyTabStr=MCwxLDIsMyw2LDQsNSw4LDcsOQ%3D%3Dhttps://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=%E5%A4%A9%E6%B0%94%E9%A2%84%E5%91%8A&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined&cs=62132575,3203655593&os=1122747204,4194965211&simid=4293052666,770807117&pn=46&rn=1&di=7060663421280190465&ln=1882&fr=&fmq=1648541792956_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=0&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fbkimg.cdn.bcebos.com%252Fpic%252Fc9fcc3cec3fdfc037c930614da3f8794a5c226b7%26refer%3Dhttp%253A%252F%252Fbkimg.cdn.bcebos.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1651133793%26t%3De9df33e8bc4e6d88e3c8d910f0a90b8e&rpstart=0&rpnum=0&adpicid=0&nojc=undefined&dyTabStr=MCwxLDIsMyw2LDQsNSw4LDcsOQ%3D%3D','https://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=%E5%A4%A9%E6%B0%94%E9%A2%84%E5%91%8A&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined&cs=2752510072,205997197&os=4000657032,1691919075&simid=2752510072,205997197&pn=53&rn=1&di=7060663421280190465&ln=1882&fr=&fmq=1648541792956_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=0&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fnimg.ws.126.net%252F%253Furl%253Dhttp%253A%252F%252Fdingyue.ws.126.net%252F2021%252F0218%252F96512b31j00qoq3yc0033c000ro00poc.jpg%2526thumbnail%253D650x2147483647%2526quality%253D80%2526type%253Djpg%26refer%3Dhttp%253A%252F%252Fnimg.ws.126.net%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1651133793%26t%3D25d7a80e9288500b9985dee75bcb712c&rpstart=0&rpnum=0&adpicid=0&nojc=undefined&dyTabStr=MCwxLDIsMyw2LDQsNSw4LDcsOQ%3D%3D','https://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=%E5%A4%A9%E6%B0%94%E9%A2%84%E5%91%8A&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined&cs=3236860548,647538631&os=1039692082,447410483&simid=3236860548,647538631&pn=58&rn=1&di=7060663421280190465&ln=1882&fr=&fmq=1648541792956_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=0&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fwww.xiazaiba.com%252Fd%252Ffile%252F2021%252F04-19%252Ficoc3a1f1112145b83890a083b119992810.png%26refer%3Dhttp%253A%252F%252Fwww.xiazaiba.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1651133793%26t%3Db290c57c6a504e7673a17b56cdf83a35&rpstart=0&rpnum=0&adpicid=0&nojc=undefined&dyTabStr=MCwxLDIsMyw2LDQsNSw4LDcsOQ%3D%3D','https://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=%E5%A4%A9%E6%B0%94%E9%A2%84%E5%91%8A&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined&cs=434514893,2677478932&os=1062291089,4068313350&simid=434514893,2677478932&pn=102&rn=1&di=7060663421280190465&ln=1882&fr=&fmq=1648541792956_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=3c&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fpic.5577.com%252Fup%252F2021-10%252F202110181829246644.png%26refer%3Dhttp%253A%252F%252Fpic.5577.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1651133795%26t%3D76a4e86be5a38266e0fa0000e89f0bf7&rpstart=0&rpnum=0&adpicid=0&nojc=undefined&dyTabStr=MCwxLDIsMyw2LDQsNSw4LDcsOQ%3D%3Dhttps://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=%E5%A4%A9%E6%B0%94%E9%A2%84%E5%91%8A&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined&cs=434514893,2677478932&os=1062291089,4068313350&simid=434514893,2677478932&pn=102&rn=1&di=7060663421280190465&ln=1882&fr=&fmq=1648541792956_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=3c&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fpic.5577.com%252Fup%252F2021-10%252F202110181829246644.png%26refer%3Dhttp%253A%252F%252Fpic.5577.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1651133795%26t%3D76a4e86be5a38266e0fa0000e89f0bf7&rpstart=0&rpnum=0&adpicid=0&nojc=undefined&dyTabStr=MCwxLDIsMyw2LDQsNSw4LDcsOQ%3D%3D','https://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=%E5%A4%A9%E6%B0%94%E9%A2%84%E5%91%8A&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined&cs=2689665208,4115011959&os=3596244740,3897763764&simid=2689665208,4115011959&pn=217&rn=1&di=7060663421280190465&ln=1882&fr=&fmq=1648541792956_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=b4&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252F5b0988e595225.cdn.sohucs.com%252Fimages%252F20190612%252Fbac7aef4fefb4c768da7f5b4a2cf5952.jpeg%26refer%3Dhttp%253A%252F%252F5b0988e595225.cdn.sohucs.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1651133823%26t%3D6743160dd448fc54cfa217e272d3adb4&rpstart=0&rpnum=0&adpicid=0&nojc=undefined&dyTabStr=MCwxLDIsMyw2LDQsNSw4LDcsOQ%3D%3D']

    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f75dba7b-cf03-4f1e-b9ab-913e5ace4ff2"  # 大
    # url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=7c978e36-fcc2-476d-9dc0-9e0950712865"    #小

    payload = json.dumps({
        "msgtype": "news",
        "news": {
            "articles": [
                {
                    "title": "测试组天气预告温馨提醒",
                    "description": result,
                    "url": "https://weathernew.pae.baidu.com/weathernew/pc?query=%E5%8C%97%E4%BA%AC%E5%A4%A9%E6%B0%94&srcid=4982",
                    "picurl": random.choice(picurl)
                }
            ]
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    pytest.main(["-v", "-s", "%sBJ_weather.py"%tpath,"--alluredir=%s"%report])