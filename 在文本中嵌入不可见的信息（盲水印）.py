# 在文本中嵌入不可见的信息（盲水印）
# pip install text_blind_watermark
from text_blind_watermark import TextBlindWatermark
# 密码
password = b"LucianaiB"
# 水印
watermark = b"shuiyin"
# 原始文本
text = '原始文本'

twm = TextBlindWatermark(pwd=password)
text_with_wm = twm.add_wm_rnd(text=text, wm=watermark)
print("加水印后的文字:",text_with_wm)


# 提取水印
from text_blind_watermark import TextBlindWatermark
# 密码
password = b"LucianaiB"
# 提取水印的文本
file_with_watermark = text_with_wm

twm = TextBlindWatermark(pwd=password)
watermark_extract = twm.extract(file_with_watermark)
print("输出水印:",watermark_extract)
