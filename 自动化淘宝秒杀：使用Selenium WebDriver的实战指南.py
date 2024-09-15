import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import win32com.client
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# 调用windows系统语音功能，可以将文字转成语音!
speaker = win32com.client.Dispatch("SAPI.SpVoice")
# 秒杀开始时间
times = '2024-09-15 17:01:00'
# 初始化webdriver
driver = webdriver.Edge()
driver.get("https://taobao.com")
time.sleep(10)
# 登录操作
driver.find_element(By.XPATH, '//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
# 最大化浏览器窗口
driver.maximize_window()
time.sleep(3)

# 进入购物车页面
driver.get("https://cart.taobao.com/cart.htm")
time.sleep(3)
# 全选购物车中的商品
driver.find_element(By.XPATH, '//*[@id="mainHeaderContainer_1"]/div[2]/label/span[1]').click()
# 循环等待秒杀时间
while True:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    print(now)
    if now > times:
        # 点击结算按钮
        driver.find_element(By.XPATH, '//*[@id="settlementContainer_1"]/div[4]/div/div[2]').click()
        # 语音提示
        # speaker.Speak("秒杀开始时间到了，请注意操作")
        break

wait = WebDriverWait(driver, 20)
element = wait.until(ec.presence_of_element_located(
    (By.CLASS_NAME, "go-btn")))
element.click()
speaker.Speak(f"主人，结算提交成功，我已帮你抢到商品啦，请即使支付订单")
