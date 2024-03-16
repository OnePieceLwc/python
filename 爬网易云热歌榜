import requests
import re
import os

# 榜单ID对应的字典
bangdan_dict = {
    '19723756': '飙升榜',
    '3779629': '新歌榜',
    '2884035': '原创榜',
    '3778678': '热歌榜'
}

print("榜单对应的ID如下:", bangdan_dict)

# 输入榜单ID
bangdan_id = input('请输入你想下载的榜单ID:')

# 输入要下载的歌曲数量
num_songs = int(input('请输入要下载的歌曲数量:'))

# 创建文件夹路径
filename = 'D:/网易云热歌榜/' + bangdan_dict[bangdan_id] + "\\"
if not os.path.exists(filename):
    os.makedirs(filename)

# 请求榜单页面
url = f"https://music.163.com/discover/toplist?id={bangdan_id}"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}
response = requests.get(url=url, headers=headers)

# 使用正则表达式提取歌曲信息
html_data = re.findall(r'<li><a href="/song\?id=(\d+)">(.*?)</a>', response.text)[:num_songs]
for song_id, title in html_data:
    # 构建音乐播放地址
    music_url = f"http://music.163.com/song/media/outer/url?id={song_id}.mp3"
    # 请求音乐播放地址并下载音乐
    music_content = requests.get(url=music_url, headers=headers).content
    # 清理文件名中的特殊字符
    cleaned_title = re.sub(r'[\\/*?:"<>|]', '', title)
    with open(os.path.join(filename, f"{cleaned_title}.mp3"), 'wb') as file:
        file.write(music_content)
    print(f"{bangdan_dict[bangdan_id]}中的{cleaned_title}.mp3下载成功")
