import requests
import time
import datetime

def my_function():
    timestamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))) # 北京时间
    try:
        response = requests.get("https://api.juejin.cn/growth_api/v1/")
        response.raise_for_status()
        print(f"[{timestamp}] API 请求成功")
    except requests.exceptions.RequestException as e:
        print(f"[{timestamp}] API 请求失败: {e}")

def check_sign_in_status(base_url, headers):
    api = "get_today_status"
    url = base_url + api
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data['err_no'] == 0:
            if data['data'] is True:
                print("【今日是否签到】", "已签到")
                return True
            elif data['data'] is False:
                print("【今日是否签到】", "未签到")
                return False
        else:
            print("【当前登录状态】", "未登录,请登录")
            pass
            return False
    else:
        print("【请求失败】", response.status_code)
        return False


def sign_in(base_url, params, headers):
    # data = '{}'
    data = ''
    url = f"{base_url}check_in"
    response = requests.post(url, headers=headers, data=data,params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                print("【当前签到状态】", "签到成功")
                return True
            elif data['err_no'] == 3013 and data['err_msg'] == "掘金酱提示：签到失败了~":
                print("【当前签到状态】", data['err_msg'])
                return False
            elif data['err_no'] == 15001:
                print("【当前签到状态】", '重复签到')
                return True
            else:
                print("【当前签到状态】", data['err_msg'])
                return False
        except requests.JSONDecodeError:
            print("【签到功能】服务器返回的数据无法解析为JSON格式。")
            return False


def get_points(base_url, headers):
    api = "get_cur_point"
    url = base_url + api
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                print("【矿石最新余额】", data['data'])
                return data['data']
        except requests.JSONDecodeError:
            print("【获取余额功能】服务器返回的数据无法解析为JSON格式。")
            return False


def get_free(base_url,params, headers):
    url = f"{base_url}lottery_config/get"
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                if data['data']['free_count'] > 0:
                    print("【免费抽奖次数】", data['data']['free_count'])
                    return True
                else:
                    print("【免费抽奖次数】", data['data']['free_count'])
                    return False
        except requests.JSONDecodeError:
            print("【获取免费抽奖次数功能】服务器返回的数据无法解析为JSON格式。")
            return False


def draw(base_url, params, headers):
    url = f"{base_url}lottery/draw"
    # data = '{}'
    data = ''
    response = requests.post(url, headers=headers, data=data,params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                print("【今日抽奖奖品】", data['data']['lottery_name'])
        except requests.JSONDecodeError:
            print("【抽奖功能】服务器返回的数据无法解析为JSON格式。")
            return False


def get_win(base_url, aid, uuid, spider, headers):
    api = "lottery_lucky/my_lucky"
    url = base_url + api
    data = {
        "aid": aid,
        "uuid": uuid,
        "spider": spider
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                total_value = data['data']['total_value']
                points = get_points(base_url, header1)
                cha = points - (6000 - total_value) * 20
                print("【当前幸运数值】：", total_value)
                if cha >= 0:
                    print("【距离中奖还差】：0 矿石！")
                elif cha <= 0:
                    print("【距离中奖还差】：", str(abs(cha)) + "矿石！")
        except requests.JSONDecodeError:
            print("【获取免费抽奖次数功能】服务器返回的数据无法解析为JSON格式。")
            return False
    else:
        print("【请求失败】", response.status_code)
        return False



if __name__ == "__main__":
    my_function()
    # 点击任意类型为fetch的网络请求
    cookie ="__tea_cookie_tokens_2608=%257B%2522web_id%2522%253A%25227419957518539048474%2522%252C%2522user_unique_id%2522%253A%25227419957518539048474%2522%252C%2522timestamp%2522%253A1727593501577%257D; is_staff_user=false; store-region=cn-sx; store-region-src=uid; passport_csrf_token=7fc71dbd5dc0576e49c067660f9b6e34; passport_csrf_token_default=7fc71dbd5dc0576e49c067660f9b6e34; odin_tt=dbfb7e6ca83b8df74cdc3b13198fe365528b4877c562e999b42474e58cef180296214579048c93fce5c6242f4ca0fa4fd66a926697db5bae5e51ed9c5aa06556; n_mh=L87qwvCoqH7EAa9jtaR8r3BZ6rOsbnMXVkE8qLt7CuY; passport_auth_status=886f1540fd258a3b5f6062fcb3c918c4%2Cddafcc94b4a6ad4c7d85082b4c0cdc5b; passport_auth_status_ss=886f1540fd258a3b5f6062fcb3c918c4%2Cddafcc94b4a6ad4c7d85082b4c0cdc5b; sid_guard=e73ddb3471e84ca868427ad557273f31%7C1745508765%7C31536000%7CFri%2C+24-Apr-2026+15%3A32%3A45+GMT; uid_tt=704cccbe11c868df045cf9cc82b24057; uid_tt_ss=704cccbe11c868df045cf9cc82b24057; sid_tt=e73ddb3471e84ca868427ad557273f31; sessionid=e73ddb3471e84ca868427ad557273f31; sessionid_ss=e73ddb3471e84ca868427ad557273f31; sid_ucp_v1=1.0.0-KDQyMzc1MTI5YzIxMzI2NTAyZjM3OTZkOGJjMzc1YWY3NDAzMjU5MjAKFwitrtDnqs2gAhCds6nABhiwFDgCQPEHGgJsZiIgZTczZGRiMzQ3MWU4NGNhODY4NDI3YWQ1NTcyNzNmMzE; ssid_ucp_v1=1.0.0-KDQyMzc1MTI5YzIxMzI2NTAyZjM3OTZkOGJjMzc1YWY3NDAzMjU5MjAKFwitrtDnqs2gAhCds6nABhiwFDgCQPEHGgJsZiIgZTczZGRiMzQ3MWU4NGNhODY4NDI3YWQ1NTcyNzNmMzE; _tea_utm_cache_2018={%22utm_source%22:%22juejin%22%2C%22utm_medium%22:%22juejin_trae%22%2C%22utm_campaign%22:%22afccsdn%22}; csrf_session_id=2811d649a4b2d945a5489ab7f7005c7c; _tea_utm_cache_2608={%22utm_source%22:%22juejin%22%2C%22utm_medium%22:%22juejin_trae%22%2C%22utm_campaign%22:%22afccsdn%22}"
    aid = "2608"
    uuid = "7419957518539048474"
    spider = "0"
    # msToken  获取后测试 url解码
    # 解密网址1:https://www.toolhelper.cn/EncodeDecode/Url
    # 解密网址2:https://www.bejson.com/enc/urlencode/index.html#google%20vignette

    msToken = 'alTCgamFmIowM_UyCs-V-RlVWatArDfnP3OEOZW8RgtOit2hnVBDv76Q3n46AiCLzDnTzXHw47xqEmxnkJpAvm2R1QmjSBOiNFjfcMerswKzmTFUOYn0yOmACHkzaiSHTRY='
    a_bogus = 'xyMQ6c2hMsm1efVzlwDz9twmuFR0YW5agZEz7ylNjtqS'
    base_url = "https://api.juejin.cn/growth_api/v1/"

    common_params = {"aid": aid, "uuid": uuid, "spider": spider, "msToken": msToken, "a_bogus": a_bogus}
    header1 = {
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
    }

    if check_sign_in_status(base_url, header1):
        if get_free(base_url,common_params, header1):
            draw(base_url,common_params, header1)
            pass
        else:
            pass
    else:
        if not sign_in(base_url, common_params, header1):
            sign_in(base_url, common_params, header1)
        if get_free(base_url,common_params, header1):
            draw(base_url, common_params, header1)
            pass
        else:
            pass
    get_win(base_url, aid, uuid, spider, header1)
