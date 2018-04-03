#coding=utf-8
import requests

r = requests.get('https://www.baidu.com/')  #向目标url地址发送get请求，返回一个response对象
print(r.text)                                #r.text是http response的网页HTML


print(type(r))