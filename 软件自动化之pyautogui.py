# 用pyautogui玩转微信及各种软件自动化
# 1.下载:pip install pyautogui
import pyautogui
# 查看屏幕尺寸，目前只支持在主屏上操作
print(pyautogui.size())
# 查看当前鼠标位置，坐标原点是屏幕左上角
print("当前鼠标位置:")
print(pyautogui.position())

# 2.移动鼠标
# 在 num_seconds 秒内将鼠标移动到 (x,y)
x,y = (500, 300)
num_seconds = 1
pyautogui.moveTo(x, y, duration=num_seconds)
# 相对路径移动，将当前位置作为坐标轴原点。
# pyautogui.moveRel(x, y, duration=num_seconds)

# 3.点击鼠标
x,y = (2357, 24)
num_of_clicks = 2   #点击次数
secs_between_clicks = 1    #点击间隔
# button：可选 LEFT、MIDDLE、RIGHT、PRIMARY（左键）或 SECONDARY（右键）。它的默认值是 PRIMARY
pyautogui.click(x=x, y=y, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
pyautogui.mouseDown()    # 按下鼠标按键（左键）
pyautogui.mouseUp()      # 释放鼠标按键（左键）

# 4.鼠标拖动
pyautogui.dragTo(x=None, y=None, duration=0.0, button='left')     # 将鼠标拖动到指定位置

# 5.鼠标滚动
pyautogui.scroll(100)   # 向上滚动100
pyautogui.scroll(-100)  # 向下滚动100
pyautogui.scroll(100, x=200, y=200)  # 移动到200， 然后执行滚动

# 6.屏幕功能
pyautogui.screenshot()    # 保存当前屏幕截图到当前目录
pyautogui.screenshot(r'C:\Users\lx\Desktop\test.png')    # 保存当前屏幕截图到指定目录
pyautogui.screenshot(r'C:\Users\lx\Desktop\test1.png', region=(300, 300, 500, 1000))    # 保存指定区域截图到指定目录

# 7.定位功能
# locateOnScreen函数，其原理是通过图像识别去匹配需要查找内容在图片中的像素区域位置
# 返回值是一个元组:(left, top, width, height)
# image识别图片的地址
# confidence是识别的准确度，默认是0.9，越大越准确，但是也会降低识别速度
# grayscale是否灰度化，默认是False，如果是True，则会将图片灰度化，提高识别速度  (以略微加速(大约 30%))
text_location = pyautogui.locateOnScreen(image='ckls.jpg', confidence=0.7,grayscale=True)
# click_btn(text_location.left/2+15, text_location.top/2+4)
print("点击了 查看历史消息")

text_location = pyautogui.locateOnScreen(image='ygz.jpg', confidence=0.7)
# click_btn(text_location.left/2+25, text_location.top/2+10)
print("点击了 已关注")

# 8.消息框功能
# PyAutoGUI 利用 PyMsgBox 中的消息框函数提供了一种跨平台的纯 Python 方法来显示 javascript 样式的消息框。
pyautogui.alert(text='text', title='title', button='alert!')   # 弹出消息框，返回 button 的值
pyautogui.confirm(text='text', title='title', buttons=['再考虑一下', '卸载'])   # 弹出确认框，返回 button 的值
pyautogui.prompt(text='text', title='title', default='请输入文本信息')   # 弹出输入框，返回文本信息

# 9.键盘控制功能
# pyautogui 并不支持输入框自动聚焦，所有输入之前先要点击输入框位置。
pyautogui.write('Hello world!', interval=0.25)    # 每个字符间隔0.25秒
pyautogui.press('num0', presses=1, interval=0.0)    # 可以用于按下任何键，包括特殊键 eg:'enter'
pyautogui.hotkey('ctrl', 'shift', 'esc')       # 接收多个字符串参数，顺序按下，再按相反的顺序释放。 相当于按下 ctrl+shift+esc 释放 esc+shift+ctrl

# 应用案例1：关注公众号太多，程序帮你批量取关
def click_btn(x,y):
    num_of_clicks = 1
    secs_between_clicks = 1
    pyautogui.click(x=x, y=y, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

# 自动化间隔
pyautogui.PAUSE = 1
for i in range(3):
    # 点开`要取关公众号`-点击`查看历史消息`
    click_btn(388,386)
    print("点击了 要取关公众号")
    click_btn(861,342)
    print("点击了 查看历史消息")
    # 点击`已关注`-点击`不再关注`，即可
    click_btn(704,373)
    print("点击了 已关注")
    click_btn(891,539)
    print("点击了 不再关注")
    break


# 再次测试自动化
import pyautogui
import time
def click_btn(x,y):
    num_of_clicks = 1
    secs_between_clicks = 1
    pyautogui.click(x=x, y=y, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

# 自动化间隔
for i in range(671):
    try:
        print(f"正在取关第{i+1}个公众号号")
        # 点开`要取关公众号`-点击`查看历史消息`
        click_btn(509,497)
        print("点击了 要取关公众号")
        text_location = pyautogui.locateOnScreen('ckls.jpg', confidence=0.7)
        click_btn(text_location.left/2+15, text_location.top/2+4)
        print("点击了 查看历史消息")
        time.sleep(1.5)
        text_location = pyautogui.locateOnScreen('ygz.jpg', confidence=0.7)
        click_btn(text_location.left/2+25, text_location.top/2+10)
        print("点击了 已关注")
        click_btn(949,620)
        print("点击了 不再关注")
    except Exception as e:
        continue
