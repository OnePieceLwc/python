import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

def down_txts(url):
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')

    # 修正查找元素的语法
    title_obj = soup.find("h1", class_="wap_none")
    con_obj = soup.find("div", id ="chaptercontent")

    if title_obj and con_obj:
        title = title_obj.get_text()  # 修正获取文本内容的方法
        title1 = con_obj.get_text()

        with open(f"D:\\小说\\{title}.txt", "w", encoding="utf-8") as f:  # 添加编码参数
            f.write(title1)
        print(f"{title}已经下载...")

starttime=datetime.now()

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

url ="https://www.bqgka.com/book/159995/"  #引入网址
res = requests.get(url , headers=headers)  #可以发送一个http get请求，返回服务器响应内容.
soup = BeautifulSoup(res.text, 'lxml')  #将文档传入BeautifulSoup，得到文档的对象
info =soup.find("div",class_="listmain").find_all("a")

urls=[]

for i in info:
    href = i["href"]
    if href != "javascript:dd_show()":
        # print(href)
        href = "https://www.bqgka.com"+href
        urls.append(href)


print(urls)

# print("单线程下载")
# for url in urls:
#     down_txts(url)

print("多线程下载")
with ThreadPoolExecutor(max_workers=len(urls)) as exe:
    for url in urls:
        exe.submit(down_txts,url)

endtime = datetime.now()
print(f"总共用,{(endtime-starttime).seconds}秒")
