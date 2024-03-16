import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

# 发送 HTTP 请求，获取页面内容
url = 'https://baike.baidu.com/item/TFBOYS?fromModule=lemma_search-box'
response = requests.get(url)
html = response.content

# 使用 Beautiful Soup 解析页面内容
soup = BeautifulSoup(html, 'html.parser')

# 提取词条的文本信息
content = soup.find('meta', {'name': 'description'})['content']
# 输出文本信息
print(content)

# 使用 jieba 分词处理 content
seg_list = jieba.cut(content, cut_all=False)
seg_list = [word for word in seg_list if len(word) > 1]  # 去除单个字的词
text = " ".join(seg_list)

# 生成词云图
wordcloud = WordCloud(font_path="simsun.ttc", background_color="white").generate(text)

# 显示词云图
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
