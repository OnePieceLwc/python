import requests
import json
import pprint
import re
import os
import subprocess
import sys

"""获取url响应体"""
def getResponse(url):
    # 设置请求头
    headers = {
        'referer': 'https://www.bilibili.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    # 发起get请求
    response = requests.get(url=url, headers=headers)
    return response

"""解析响应体"""
def parseResponse(url):
    # 获取url响应体
    response = getResponse(url)
    # 用正则表达式取出返回的视频数据
    html_data = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]
    # 解析成json数据
    jsonData = json.loads(html_data)
    # 获取视频标题
    videoTitle = re.findall('<title data-vue-meta="true">(.*?)</title>', response.text)[0]
    # 获取音频
    audioUrl = jsonData['data']['dash']['audio'][0]['baseUrl']
    # 获取视频
    videoUrl = jsonData['data']['dash']['video'][0]['baseUrl']
    # 封装视频信息
    videoInfo = {
        'videoTitle': videoTitle,
        'audioUrl': audioUrl,
        'videoUrl': videoUrl,
    }
    print("获取Response信息成功！")
    return videoInfo

"""保存视频和音频"""
def saveMedia(fileName, content, mediaType):
    # 创建目录（如果不存在）
    os.makedirs('D:\\bilibili', exist_ok=True)
    # 写入文件
    with open(f'D:\\bilibili\\{fileName}.{mediaType}', mode='wb') as f:
        f.write(content)
    print(f"保存{mediaType}成功！")

def AvMerge(Mp3Name, Mp4Name, savePath):
    print("开始合并音频和视频.........")
    print(f"音频文件: {Mp3Name}")
    print(f"视频文件: {Mp4Name}")
    print(f"合并后文件保存路径: {savePath}")

    # 使用subprocess来调用ffmpeg，并重定向输出
    with open(os.devnull, 'w') as devnull:
        result = subprocess.run(
            ['ffmpeg', '-i', Mp4Name, '-i', Mp3Name, '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', savePath],
            stdout=devnull,
            stderr=devnull
        )

    print("合并成功！")
    os.remove(Mp3Name)
    os.remove(Mp4Name)

def main():
    url = input("请输入B站视频url地址:")
    videoInfo = parseResponse(url)
    # 获取视频标题
    fileName = videoInfo['videoTitle']
    # 下载并保存音频
    audioContent = getResponse(videoInfo['audioUrl']).content
    saveMedia(fileName, audioContent, 'mp3')
    # 下载并保存视频
    videoContent = getResponse(videoInfo['videoUrl']).content
    saveMedia(fileName, videoContent, 'mp4')

    Mp3Name = f'D:\\bilibili\\{fileName}.mp3'
    Mp4Name = f'D:\\bilibili\\{fileName}.mp4'
    savePath = f'D:\\bilibili\\merge_{fileName}.mp4'
    AvMerge(Mp3Name, Mp4Name, savePath)


if __name__ == '__main__':
    main()
