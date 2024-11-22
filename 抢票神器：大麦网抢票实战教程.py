import os
import time
import pickle
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 抢票相关页面
# 大麦网主页
damai_url = "https://www.damai.cn/"
# 登录页
login_url = "https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F"
# 抢票目标页
target_url = 'https://detail.damai.cn/item.htm?spm=a2oeg.home.card_0.ditem_1.2bbb23e1uo54LV&id=853329221023'

# 定义具体类
class Concert:
    def __init__(self):
        self.status = 0         # 状态,表示如今进行到何种程度
        self.login_method = 1   # {0:模拟登录,1:Cookie登录}自行选择登录方式
        self.driver = webdriver.Chrome()       # 默认Chrome浏览器
        self.execute_stealth_script(self)  # 执行stealth脚本

    # 执行stealth脚本
    # 机器检测问题，使用的driver会被识别为机器人，无法欺骗到检测程序，这里我们使用stealth.min.js进行解决。
    @staticmethod
    def execute_stealth_script(self):
        with open('stealth.min.js', 'r') as f:
            js = f.read()
            self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js})
            print('###已执行stealth脚本###')

    # 通过cookie进行登陆
    # 在Concert类中login_method = 1时才会使用到，便于快速登陆，省去登陆过程，其中初次运行代码时，用户登陆后会在本地生成cookies.pkl文件来存储cookie信息，用于快速登陆。
    def set_cookie(self):
        self.driver.get(damai_url)
        print("###请点击登录###")
        while self.driver.title.find('大麦网-全球演出赛事官方购票平台') != -1:
            sleep(1)
        print('###请扫码登录###')

        while self.driver.title != '大麦网-全球演出赛事官方购票平台-100%正品、先付先抢、在线选座！':
            sleep(1)
        print("###扫码成功###")
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))
        print("###Cookie保存成功###")
        self.driver.get(target_url)


    def get_cookie(self):
        try:
            cookies = pickle.load(open("cookies.pkl", "rb"))  # 载入cookie
            for cookie in cookies:
                cookie_dict = {
                    'domain':'.damai.cn',  # 必须有，不然就是假登录
                    'name': cookie.get('name'),
                    'value': cookie.get('value')
                }
                self.driver.add_cookie(cookie_dict)
            print('###载入Cookie###')
        except Exception as e:
            print(e)

    # 登陆
    def login(self):
        if self.login_method == 0:
            self.driver.get(login_url)
            # 载入登录界面
            print('###开始登录###')

        elif self.login_method == 1:
            if not os.path.exists('cookies.pkl'):
                # 如果不存在cookie.pkl,就获取一下
                self.set_cookie()
            else:
                self.driver.get(target_url)
                self.get_cookie()

    # 打开浏览器
    def enter_concert(self):
        """打开浏览器"""
        print('###打开浏览器，进入大麦网###')
        self.driver.maximize_window()           # 最大化窗口
        # 调用登陆
        self.login()                            # 先登录再说
        # self.driver.refresh()                   # 刷新页面
        self.status = 2                         # 登录成功标识
        print("###登录成功###")


    # 选择票型
    def choose_ticket(self):
        if self.status == 2:                  #登录成功入口
            print("="*30)
            print("###检查是否开始售票###")
            # while not self.isElementExistByClass('buy-link'):
            #     self.driver.refresh()
            #     print("###售票尚未开始,刷新等待开始###")
            # TODO 选择票型
            #========begin=========
            # 选择具体票型部分未写，该部分可自行添加，不添加的话，自行选择进入页面后大麦的默认选择。
            #========end===========
            self.driver.find_element(By.CLASS_NAME, 'buybtn').click()    #点击购票二维码下的购买连接
            time.sleep(1.5)
            self.check_order()

    # 确认订单
    def check_order(self):
        if self.status == 2:
            print('###开始确认订单###')
            if self.driver.title == '订单确认页':
                print('###检查是否需要填写观影人')
                # if self.isElementExistByXPATH('//*[@id="dmViewerBlock_DmViewerBlock"]'):
                #     self.driver.find_element(By.XPATH, '//*[@id="dmViewerBlock_DmViewerBlock"]/div[2]/div/div').click()
                #     time.sleep(0.5)
                # time.sleep(60)
                print('###跳转支付选择界面###')
                self.driver.find_element(By.XPATH, '//*[@id="dmOrderSubmitBlock_DmOrderSubmitBlock"]/div[2]/div/div[2]/div[2]/div[2]/span').click()
                time.sleep(2)
                self.pay_order()

    # 支付宝登陆支付
    def pay_order(self):
        if self.driver.title == "支付宝付款":
            print('###支付订单###')
            time.sleep(60)
            self.driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div[1]/button[2]').click()
            print('###跳转至浏览器支付###')
            time.sleep(1.5)
            self.driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div[1]/div[2]/input').clear()
            self.driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div[1]/div[2]/input').send_keys('支付宝账号')      #输入支付宝账号
            self.driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/button').click()
            time.sleep(1.5)
            self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/button').click()
            while True:
                time.sleep(1)
                print('###请输入支付密码###')

    # 脚本结束退出
    def finish(self):
        self.driver.quit()

if __name__ == '__main__':
    try:
        con = Concert()  # 初始化函数
        con.enter_concert()  # 打开浏览器
        con.choose_ticket()  # 开始抢票

    except Exception as e:
        print(e)
        con.finish()
