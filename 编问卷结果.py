# 修改题目数量和比例

import datetime
#获取当天的日期,并进行格式化,用于后面文件命名，格式:20200420
today = datetime.date.today().strftime('%Y%m%d')
print(today)
import random

def generate_data(total_samples):
    data = []

    # 问题18: 陪伴旅行风格（修改后）
    travel_style_options = ['A. 全托', 'B. 半托']
    travel_style_weights = [0.47, 0.53]

    for _ in range(total_samples):
        # 随机选择一个选项
        choice = random.choices(travel_style_options, weights=travel_style_weights)[0]
        data.append({'问题18: 陪伴旅行风格': choice})

    return data

if __name__ == "__main__":
    total_samples = 206
    generated_data = generate_data(total_samples)

    # 打印生成的数据
    for i, item in enumerate(generated_data, start=1):
        print(f"样本{i}: {item['问题18: 陪伴旅行风格']}")
