from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# 初始化webdriver
wd = webdriver.Chrome()
wd.maximize_window()
wd.implicitly_wait(5)

# 打开微信公众号平台
wd.get('https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=835840104')

# 登录流程
wd.find_element(By.ID, 'jumpUrl').click()
wd.find_element(By.XPATH, "//a[@class='login__type__container__select-type']").click()
wd.find_element(By.CSS_SELECTOR, "input[name='account']").send_keys('账号')
wd.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys('密码')
wd.find_element(By.CLASS_NAME, 'btn_login').click()

# 等待用户扫码
time.sleep(10)

# 点击图文消息
wd.find_element(By.XPATH, "//*[@id='app']/div[2]/div[4]/div[2]/div/div[1]/div").click()

# 切换到新窗口
wd.switch_to.window(wd.window_handles[-1])

# 输入标题和作者
wd.find_element(By.XPATH, "//*[@id='title']").send_keys('标题')
wd.find_element(By.XPATH, "//*[@id='author']").send_keys('作者')

# 切换到iframe并输入文章内容
wd.switch_to.frame(wd.find_element(By.XPATH, '//*[@id="ueditor_0"]'))
wd.find_element(By.XPATH, "/html/body/p").send_keys('文章内容')
wd.switch_to.default_content()

# 滚动到封面选择区域并选择封面
target = wd.find_element(By.XPATH, '//*[@id="js_cover_area"]/div[1]/span')
wd.execute_script("arguments[0].scrollIntoView();", target)

# 鼠标悬停并选择封面
ac = ActionChains(wd)
ac.move_to_element(target).perform()
time.sleep(1)
wd.find_element(By.XPATH, '//*[@id="js_cover_null"]/ul/li[2]/a').click()

# 选择第一张图片并点击下一步
wd.find_element(By.XPATH, '//*[@id="js_image_dialog_list_wrp"]/div/div[1]/i').click()
wd.find_element(By.XPATH, '//*[@id="vue_app"]/div[2]/div[1]/div/div[3]/div[1]/button').click()
wd.find_element(By.XPATH, '//*[@id="vue_app"]/div[2]/div[1]/div/div[3]/div[2]/button').click()

# 清除简介信息
wd.find_element(By.XPATH, '//*[@id="js_description"]').clear()

# 鼠标悬停并点击写新图文
ac.move_to_element(wd.find_element(By.XPATH, '//*[@id="js_add_appmsg"]/i')).perform()
wd.find_element(By.XPATH, '/html/body/div[18]/div/ul/li[1]/a').click()

# 点击群发
wd.find_element(By.XPATH, '//*[@id="js_send"]/button/span').click()
