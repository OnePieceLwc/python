import requests
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


def hot_search():
    url = 'https://weibo.com/ajax/side/hotSearch'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()['data']


from urllib.parse import quote
from datetime import datetime
print(datetime.now().strftime('微博热搜榜 20%y年%m月%d日 %H:%M'))
def main(num):
    data = hot_search()
    if not data:
        print('获取微博热搜榜失败')
        return
    print(f"置顶:{data['hotgov']['word'].strip('#')}")
    for i, rs in enumerate(data['realtime'][:num], 1):
        title = rs['word']
        try:
            label = rs['label_name']
            if label in ['新', '爆', '沸']:
                label = label
            else:
                label = ''
        except:
            label = ''

        # print(f"{i}. {title} {label}")
        link = (f"链接：https://s.weibo.com/weibo?q={quote(title)}&Refer=top")
        print(f"{i}. {title} {label} 链接：https://s.weibo.com/weibo?q={quote(title)}&Refer=top ")


if __name__ == '__main__':
    num = 20  # 获取热搜的数量
    main(num)
