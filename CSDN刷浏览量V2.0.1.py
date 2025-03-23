import re
import yaml
import json
import time
import random
import requests
from loguru import logger

# 配置文件路径
CONFIG_FILE = "config.yaml"

# 读取配置文件
try:
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    logger.critical(f"配置文件 {CONFIG_FILE} 未找到!")
    exit(1)
except yaml.YAMLError as e:
    logger.critical(f"解析配置文件 {CONFIG_FILE} 失败: {e}")
    exit(1)

# 获取配置参数
csdn_rss_url = config.get("csdnRRS", {}).get("url")

if not csdn_rss_url:
    logger.critical("配置文件中缺少 csdnRRS.url 参数!")
    exit(1)

proxy_api_url = config.get("proxy_api", {}).get("url")
if not proxy_api_url:
    logger.critical("配置文件中缺少 proxy_api.url 参数!")
    exit(1)

# 初始化日志
logger.add("logs/{time:YYYY-MM-DD}.log", rotation="00:00", retention="7 days")


def fetch_proxies(api_url):
    """从API获取代理IP列表，处理嵌套的JSON结构"""
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()

        data = response.json()
        if not isinstance(data, dict) or 'data' not in data or 'list' not in data['data']:
            logger.error(f"API返回的数据格式不正确: {data}")
            return []

        proxies = []
        for proxy_data in data['data']['list']:
            if 'ip' in proxy_data and 'port' in proxy_data:
                proxies.append(f"{proxy_data['ip']}:{proxy_data['port']}")

        return proxies

    except requests.exceptions.RequestException as e:
        logger.error(f"获取代理失败: {e}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"解析代理JSON失败: {e}, Raw response: {response.text}")
        return []
    except KeyError as e:
        logger.error(f"JSON中缺少必要的键: {e}, Raw response: {response.text}")
        return []
    except Exception as e:
        logger.exception(f"获取代理发生未知错误: {e}")
        return []


def get_links_from_rss(rss_url, headers):
    """从RSS获取链接"""
    try:
        response = requests.get(rss_url, headers=headers, timeout=10)
        response.raise_for_status()
        links = re.findall(r'<link>(.*?)</link>', response.text)
        return links
    except requests.exceptions.RequestException as e:
        logger.error(f"获取RSS链接失败: {e}")
        return []
    except Exception as e:
        logger.exception(f"获取RSS链接发生未知错误: {e}")
        return []

def run():
    """主函数"""
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    proxies = fetch_proxies(proxy_api_url)
    if not proxies:
        logger.error("没有获取到任何代理IP，程序退出。")
        return

    links = get_links_from_rss(csdn_rss_url, headers)
    if not links:
        logger.error("没有获取到任何RSS链接，程序退出。")
        return

    for proxy in proxies:
        for link in random.sample(links, len(links) - 5):
            logger.info(f"使用代理 {proxy} 访问链接 {link}")
            time.sleep(random.uniform(5, 10))  # 随机等待5-10秒


if __name__ == '__main__':
    run()
