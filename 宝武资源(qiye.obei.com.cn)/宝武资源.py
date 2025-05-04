import requests
import json
import re


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://qiye.obei.com.cn",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://qiye.obei.com.cn/web-zone/bwzy/procurement.html",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    # "x-csrf-token": "vteJjSyWL3QiF5s_fJPE2-EV"
}
url = "https://qiye.obei.com.cn/web-zone/api/sys/zone/getPurchaseList"
data = {
    "code": "bwzy",
    "noticeType": "1",
    "pageNum": 1,
    "pageSize": 10,
    "pageFlag": "addSelect",
    "sidx": "issueDate",
    "sord": "desc"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

cookies=response.cookies

# 将 cookies 转换为字符串
cookies_str = str(cookies)

# 使用正则表达式提取 csrfToken 的值
match = re.search(r'csrfToken=([^;]+)', cookies_str)

csrf_token = match.group(1).split(' for ')[0]

def get_data(page,csrf_token):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://qiye.obei.com.cn",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://qiye.obei.com.cn/web-zone/bwzy/procurement.html",
        "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
        "x-csrf-token": csrf_token
    }

    json_data = {
        'code': 'bwzy',
        'noticeType': '2',
        # 'pageNum': 4,
        'pageSize': 10,
        'pageFlag': 'addSelect',
        'sidx': 'requestEndDate',
        'sord': 'desc',
    }
    cookies = {
        'csrfToken': csrf_token,
        # 其他cookie键值对
    }

    json_data['pageNum']=page

    response = requests.post('https://qiye.obei.com.cn/web-zone/api/sys/zone/getMakeList',cookies=cookies,headers=headers,json=json_data,)
    print(response.json())


for i in range(1, 11):
    get_data(i,csrf_token)