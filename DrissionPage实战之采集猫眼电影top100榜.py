# -*- encoding:utf-8 -*-
import logging
from DrissionPage import ChromiumPage
from DataRecorder import Recorder

# 设置日志记录器
logging.basicConfig(
    filename='data.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 创建页面对象
page = ChromiumPage()
# 创建记录器对象
recorder = Recorder('data.csv')

# 访问网页
page.get('https://www.maoyan.com/board/4')

while True:
    # 遍历页面上所有 dd 元素
    for mov in page.eles('t:dd'):
        # 获取所需的信息
        num = mov('t:i').text
        score = mov('.score').text
        title = mov('@data-act=boarditem-click').attr('title')
        star = mov('.star').text
        time = mov('.releasetime').text

        # 写入到记录器
        recorder.add_data((num, title, star, time, score))

        # 记录中文信息
        logging.debug(f'记录电影信息: {num}, {title}, {star}, {time}, {score}')

    # 获取下一页按钮，有就点击
    btn = page('下一页', timeout=2)
    if btn:
        btn.click()
        page.wait.load_start()  # 等待页面加载
    else:
        break

# 记录数据
recorder.record()
