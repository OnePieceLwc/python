import pyttsx3

# 初始化引擎
engine = pyttsx3.init()

engine.setProperty('rate', 125)     #调整语速，设置为125

engine.setProperty('volume', 1.0)     #调整音量,范围在[0，1]

voices = engine.getProperty('voices')   # 获取所有的声音，包括不同语言

# for voice in voices:
    # print(voice)    # 打印所有可用的声音

# 中文声音的 ID，通常是 'com.apple.voice.compact.zh-N.Tingting'
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0')  # 设置本机的中文声音

# 让引擎说话
engine.say("你好，我会说这段文字。")
engine.runAndWait()
