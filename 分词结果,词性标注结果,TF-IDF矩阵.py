# 导入所需的库
import jieba
import jieba.posseg as pseg
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import re

with open("C:\\Users\\lx\\Desktop\\南方周末新年献词.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 1. 语词切割采用精确分词
seg_list = jieba.cut(text, cut_all=False)

# 2. 去除停用词
stop_words = ["的", "了", "和", "是", "在", "有", "也", "与", "对", "中", "等"]
filtered_words = [word for word in seg_list if word not in stop_words]

# 3. 标准化
# 去除标点符号、数字、特殊符号等
# filtered_words = [re.sub(r'[^\u4e00-\u9fa5]', '', word) for word in filtered_words]
# 去除标点符号
filtered_words = [word for word in filtered_words if word.strip()]

# 4. 词性标注采用jieba.posseg
words = pseg.cut("".join(filtered_words))

# 5. 构建语词文档矩阵(TF-IDF算法)
corpus = [" ".join(filtered_words)]  # 将处理后的文本转换为列表形式
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# 输出结果
print("分词结果：", "/".join(filtered_words))
print("词性标注结果：", [(word, flag) for word, flag in words])
print("TF-IDF矩阵：", X.toarray())

import pandas as pd

# 将TF-IDF矩阵转换为DataFrame
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# 重塑DataFrame，将词语和权值放在一列中
df_melted = df.melt(var_name='word', value_name='weight')

# 将DataFrame输出到Excel表中
df_melted.to_excel("C:\\Users\\lx\\Desktop\\2024.xlsx", index=False)
