import requests
from lxml import etree

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://finance.sina.com.cn/stock/",
    "^sec-ch-ua": "^\\^Chromium^^;v=^\\^9^^, ^\\^Not?A_Brand^^;v=^\\^8^^^",
    "sec-ch-ua-mobile": "?0",
    "^sec-ch-ua-platform": "^\\^Windows^^^",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.6.2081 SLBChan/105 SLBVPV/64-bit"
}
cookies = {
    "UOR": "www.baidu.com,finance.sina.com.cn,",
    "SINAGLOBAL": "223.160.141.105_1741230958.531690",
    "Apache": "223.160.141.143_1741704337.763544",
    "ULV": "1741704387339:6:6:2:223.160.141.143_1741704337.763544:1741704337688"
}
url = "https://zhibo.sina.com.cn/api/zhibo/feed"
params = {
    "zhibo_id": "152",
    "id": "",
    "tag_id": "0",
    "page": "1",
    "page_size": "20",
    "type": "0",
    # "callback": "t17417483"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

res=response.json()

r=[]
items=dict()

for item in res['result']['data']['feed']['list']:
    items = dict()
    items['content']=item['rich_text']
    items['datatime']=item['create_time']
    r.append(items)

for i in r:
    print(i)