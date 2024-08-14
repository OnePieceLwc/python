# -*- encoding:utf-8 -*-
from DrissionPage import ChromiumPage
import os
import requests

from TimePinner import Pinner  # 导入计时工具
pinner = Pinner()  # 创建计时器对象
pinner.pin()  # 标记开始记录
# 创建页面对象
page = ChromiumPage()

# 创建保存图片的目录
save_dir = './imgs'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 访问目标网页
page.get('https://bz.zzzmh.cn/index')

# 爬取2页，给作者省点流量
for _ in range(2):
    # 遍历一页中所有壁纸图片
    for button in page.s_eles('.down-span'):
        # 获取封面图片对象
        a = button('t:a')
        img_url = a.attr('href')
        print(img_url)  # 打印图片链接

        # 保存图片
        response = requests.get(img_url, stream=True)
        img_name = img_url.split('/')[-1].split('.')[0] + '.jpg'
        img_path = os.path.join(save_dir, img_name)
        with open(img_path, 'wb') as f:
            f.write(response.content)
        print(f"图片已保存: {img_path}")

    # 点击下一页
    next_button = page('下一页')
    if next_button:
        next_button.click()
        page.wait.load_start()  # 等待页面加载
    else:
        break

pinner.pin('用时')  # 记录并打印时间

