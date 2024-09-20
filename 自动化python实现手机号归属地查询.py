import argparse
from phone import Phone

'''
官方文档：https://github.com/ls0f/phone
pip地址：https://pypi.org/project/phone
'''

# 创建 Phone 实例
p = Phone()

def parse_phone_num(phone_num: str) -> dict:
    """使用 find 方法解析电话号码"""
    return p.find(phone_num)

def getIpRegin(ip: str) -> dict:
    """模拟的IP归属地查询函数"""
    return {
        "ip": ip,
        "country": "中国",
        "region": "某省",
        "city": "某市"
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='通过电话号码或IP地址查询归属地信息')
    parser.add_argument('-p', dest='phone', help='通过电话号码查询归属地')
    parser.add_argument('-i', dest='ip', help='通过IP地址查询归属地')
    args = parser.parse_args()

    if args.phone:
        phone_info = parse_phone_num(args.phone)
        # 中文输出格式
        print(f'电话号码: {args.phone}')
        print(f'省份: {phone_info.get("province", "未知")}')
        print(f'城市: {phone_info.get("city", "未知")}')
        print(f'邮政编码: {phone_info.get("zip_code", "未知")}')
        print(f'区号: {phone_info.get("area_code", "未知")}')
        print(f'电话类型: {phone_info.get("phone_type", "未知")}')

    if args.ip:
        ip_info = getIpRegin(args.ip)
        print(f'IP地址: {args.ip}')
        print(f'国家: {ip_info["country"]}')
        print(f'省份: {ip_info["region"]}')
        print(f'城市: {ip_info["city"]}')

# 直接查询电话号码
if __name__ == '__main__':
    phone_number = "电话"
    phone_info = parse_phone_num(phone_number)
    # 中文输出格式
    print(f'电话号码: {phone_number}')
    print(f'省份: {phone_info.get("province", "未知")}')
    print(f'城市: {phone_info.get("city", "未知")}')
    print(f'邮政编码: {phone_info.get("zip_code", "未知")}')
    print(f'区号: {phone_info.get("area_code", "未知")}')
    print(f'电话类型: {phone_info.get("phone_type", "未知")}')
