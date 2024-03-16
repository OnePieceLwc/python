import jieba
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 爬取百度百科“TFBOYS”词条的内容
url = 'https://baike.baidu.com/item/TFBOYS?fromModule=lemma_search-box'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
content_meta = soup.find('meta', {'name': 'description'})
content_text = content_meta['content']

# 使用jieba库对词条内容进行分词
words = jieba.cut(content_text)

# 将分词结果转换为列表，并去除单个字的词
words_list = [word for word in words if len(word) > 1]

# 生成词云图
if len(words_list) > 0:
    wordcloud = WordCloud(font_path='msyh.ttc', background_color='white', width=800, height=600).generate(' '.join(words_list))
    wordcloud.to_file('D:\低频震荡的参数识别\TFBOYS.png')
    plt.figure(figsize=(8, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # 隐藏坐标轴
    plt.show()

    print("词云图已生成")
else:
    print("没有找到词条内容")
