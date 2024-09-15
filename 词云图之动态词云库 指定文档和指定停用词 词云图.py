import jieba
from pyecharts import options as opts
from pyecharts.charts import WordCloud

# 读入原始数据
text_road = 'C:\\Users\\lx\\Desktop\\南方周末新年献词.txt'
# 对文章进行分词
text = open(text_road, 'r', encoding='utf-8').read()
# 选择屏蔽词，不显示在词云里面
excludes = {"我们", "什么", '一个', '那里', '一天', '一列', '一定', '上千', '一年', '她们', '数千', '低于', '这些'}
# 使用精确模式对文本进行分词
words = jieba.lcut(text)
# 通过键值对的形式存储词语及其出现的次数
counts = {}

for word in words:
    if len(word) == 1:  # 单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word, 0) + 1  # 遍历所有词语，每出现一次其对应的值加 1
for word in excludes:
    del counts[word]
items = list(counts.items())  # 将键值对转换成列表
items.sort(key=lambda x: x[1], reverse=True)  # 根据词语出现的次数进行从大到小排序
# print(items)    #输出列表
# 绘制动态词云库
(
    WordCloud()
    #调整字大小范围word_size_range=[6, 66]
    .add(series_name="南方周末新年献词", data_pair=items, word_size_range=[6, 66])
    #设置词云图标题
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="南方周末新年献词", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    #输出为词云图
    .render_notebook()
)
