import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from imageio import imread

# 读取文本数据
text = open('work/中文词云图.txt', 'r', encoding='utf-8').read()
# 读取停用词，创建停用词表
stopwords = [line.strip() for line in open('work/停用词.txt', encoding='UTF-8').readlines()]
# 对文章进行分词
words = jieba.cut(text, cut_all=False, HMM=True)

# 对文本清洗，去掉单个词
mytext_list = []
for seg in words:
    if seg not in stopwords and seg != " " and len(seg) != 1:
        mytext_list.append(seg.replace(" ", ""))
cloud_text = ",".join(mytext_list)
# 读取背景图片
jpg = imread('"C:\Users\lx\Desktop\大学\指定文档和指定停用词.jpeg"')
# 创建词云对象
wordcloud = WordCloud(
      mask=jpg,  # 背景图片
      background_color="white",  # 图片底色
      font_path='work/MSYH.TTC',  # 指定字体
      width=1500,  # 宽度
      height=960,  # 高度
      margin=10
).generate(cloud_text)

# 绘制图片
plt.imshow(wordcloud)
# 去除坐标轴
plt.axis("off")
# 显示图像
plt.show()
