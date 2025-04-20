import requests
import multiprocessing
import time
import random
import logging
import os

# 建立日志文件夹和日志文件
log_dir = "log"
log_file = os.path.join(log_dir, "requests.log")

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(filename=log_file, level=logging.INFO, filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')


success_num = 0
CONSTANT = 0

def brash(proxy_dict):
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    UserAgent = random.choice(user_agent_list)
    header = {'User-Agent': UserAgent}

    try:
        r = requests.get("https://blog.csdn.net/lwcwam/article/details/147377549", headers=header, proxies=proxy_dict, timeout=10)
        r.raise_for_status()
        logging.info("Request successful") # 成功日志
        print("successful")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}") # 失败日志
        print(f"failed: {e}")
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}") # 异常日志
        print(f"An unexpected error occurred: {e}")
    time.sleep(1)
    return None


if __name__ == '__main__':
    final = 2000
    count = 1
    for _ in range(final):
        proxies = [{'http': 'https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=1000&page=1&language=zh-hans'}]
        for _ in range(count):
            pool = multiprocessing.Pool(processes=32)
            results = [pool.apply_async(brash, (proxy,)) for proxy in proxies if proxy]
            for result in results:
                result.get()
            pool.close()
            pool.join()
