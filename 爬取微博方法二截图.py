import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 配置浏览器选项
opts = Options()
mobile_emulation = {"deviceMetrics": {"width": 375, "height": 667, "pixelRatio": 2.0},"userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/116.0.0.0"}
opts.add_experimental_option("mobileEmulation", mobile_emulation)
# opts.add_argument('--headless')  # 启用无头模式
# 创建浏览器
driver = webdriver.Edge(options=opts)
driver.set_window_size(375, 750)  # 窗口大小
name = datetime.now().strftime('20%y年%m月%d日%H:%M')
# 导航到要截图的页面
url = 'https://s.weibo.com/top/summary?cate=realtimehot'
driver.get(url)

# 截取整个页面
print("正在运行，请稍后……")
#
time.sleep(10)
screenshot = driver.get_screenshot_as_file(f'screenshot/{name}.png')
# 关闭浏览器
driver.quit()
print("运行完毕，请于文件夹中查看")
