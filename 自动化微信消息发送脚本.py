import pyperclip
import pyautogui
import time

pyautogui.PAUSE = 1

def findWindow():
    windows = pyautogui.getWindowsWithTitle('微信')
    if len(windows) == 0:
        raise Exception("微信窗口未找到")
    return windows[0]

def clickAvatar():
    try:
        location = pyautogui.locateOnScreen('C:\\Users\\lx\\Desktop\\08.png')
        if location is None:
            print('头像未找到，检查图像是否存在于屏幕上')
            return
        pyautogui.click(location)
    except pyautogui.ImageNotFoundException:
        print('头像未找到，抛出异常')

def clickSend():
    try:
        location = pyautogui.locateOnScreen('C:\\Users\\lx\\Desktop\\45.png')
        if location is None:
            print('发送按钮未找到，检查图像是否存在于屏幕上')
            return
        pyautogui.click(location.left, location.top)
    except pyautogui.ImageNotFoundException:
        print('发送按钮未找到，抛出异常')

def paste(content):
    pyperclip.copy(content)
    pyautogui.hotkey('ctrl', 'v')

if __name__ == '__main__':
    wxWindow = findWindow()
    wxWindow.activate()  # 激活窗口
    time.sleep(2)  # 等待窗口完全激活
    clickAvatar()

    content = '你好'
    paste(content)

    clickSend()
