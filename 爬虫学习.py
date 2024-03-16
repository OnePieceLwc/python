# 爬虫的过程，就是模仿浏览器的行为，往目标站点发送请求，接收服务器的响应数据，提取需要的信息，并进行保存的过程。

# 上网的全过程:
#     普通用户:
#         打开浏览器 --> 往目标站点发送请求 --> 接收响应数据 --> 渲染到页面上。
#     爬虫程序:
#         模拟浏览器 --> 往目标站点发送请求 --> 接收响应数据 --> 提取有用的数据 --> 保存到本地/数据库.

# 爬虫的过程：
#     1.发送请求（requests模块）
#     2.获取响应数据（服务器返回）
#     3.解析并提取数据（BeautifulSoup查找或者re正则）
#     4.保存数据

# #在请求网页爬取的时候，输出的text信息中会出现抱歉，无法访问等字眼
# #headers是解决requests请求反爬的方法之一，相当于我们进去这个网页的服务器本身，假装自己本身在爬取数据。
# #在谷歌浏览器搜索:chrome://version/   复制粘贴其中的用户代理部分
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

# Python为爬虫的实现提供了工具:
import requests
#   requests模块:requests是python实现的简单易用的HTTP库。
url ="https://news.baidu.com/"  #引入网址
# url ="http://www.zuel.edu.cn/2020n/list.htm"  #引入网址
# url ="http://httpbin.org/get"  #引入网址
res = requests.get(url , headers=headers)  #可以发送一个http get请求，返回服务器响应内容.
# payload = {'key1': 'value1', 'key2': 'value2'}   #传递 URL 参数
# res = requests.get(url , headers=headers , params=payload)  #可以发送一个http get请求，返回服务器响应内容.
res.encoding = 'utf-8'   #将编码格式转变成中文格式
# print(res)
print(res.url)    #传递 URL 参数
# print(res.json())    #将响应体解析为 JSON 格式的数据
# print(res.text)    #显示所获取的资源的内容
print(res.status_code)    #显示所获取的资源的响应状态码
print(res.headers['content-type'])    #显示所获取的资源的响应头中 content-type 的值

import re
result=re.findall("<title>(.*?)</title>",res.text)
print(result)  #爬取网站标题
# result1=re.findall("title='(.*?)'>",res.text)    #使用re.findall来查找所有的title标签
# print(result1)  #爬取所有的title标签

from bs4 import BeautifulSoup
#   BeautifulSoup库:BeautifulSoup 是一个可以从HTML或XML文件中提取数据的Python库。
# BeautifulSoup(markup, "html.parser")或者BeautifulSoup(markup, "lxml")，推荐使用lxml作为解析器,因为效率更高.
# soup = BeautifulSoup(res.text, 'html.parser')  #将文档传入BeautifulSoup，得到文档的对象
# print(soup)
soup = BeautifulSoup(res.text, 'lxml')  #将文档传入BeautifulSoup，得到文档的对象
# print(soup)

# 这些新闻都是位于一个class为mod-tab-content的<div>内，返回该标签
info = soup.find("div",class_="mod-tab-content").find_all("ul")
#然后查看每一条新闻的具体内容，发现所需内容在标签</a>内
for i in info:
    l = i.find_all("a")
    for j in l:
        site = j.get("href")  #查找网址链接
        title = j.get_text()   #查找新闻标题
        print(title,site)
