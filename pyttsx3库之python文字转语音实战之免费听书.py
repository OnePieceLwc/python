#  1.http://www.shuyy8.cc/book/24/#download    #下载小说txt文件
#  2.使用代码

import pyttsx3

def read_novel(novel_text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # 设置语速
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0')  # 设置中文声音

    # 分段读取小说文本
    paragraphs = novel_text.split("\n")
    for paragraph in paragraphs:
        # 这一段没有内容的，就不读了
        if len(paragraph) > 0:
            engine.say(paragraph)
            engine.runAndWait()

    engine.stop()

if __name__ == "__main__":
    # 读取小说文本文件
    with open("盗墓笔记.txt", "r", encoding="utf-8") as file:
        novel_text = file.read()

    read_novel(novel_text)
