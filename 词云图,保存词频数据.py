import os
from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
import matplotlib.font_manager
import pandas as pd

# 读取文本文件
file_path = r"C:\Users\lx\Desktop\南方周末新年献词.txt"  # 在文件路径前加上r，表示原始字符串
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# 使用结巴分词对中文文本进行分词处理
seg_list = jieba.cut(text, cut_all=False)
seg_list = [word for word in seg_list if len(word) > 1]  # 去除单个字的词

# 将分词结果拼接成字符串
seg_text = " ".join(seg_list)

# 使用统计数据生成词云图，并指定字体
font_path = "C:\\Windows\\Fonts\\simhei.ttf"  # 替换为您系统中的中文字体路径
wordcloud = WordCloud(width=800, height=400, font_path=font_path, background_color='white').generate(seg_text)

# 绘制并显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# 计算词频
word_freq = wordcloud.words_

# 将词频数据转换为DataFrame
df = pd.DataFrame(list(word_freq.items()), columns=['word', 'weight'])

# 将DataFrame保存为Excel文件
output_file_path = r"C:\Users\lx\Desktop\2024词云图.xlsx"
df.to_excel(output_file_path, index=False)
