import requests
import json
import csv

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://ygp.gdzwfw.gov.cn",
    "Referer": "https://ygp.gdzwfw.gov.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/105 SLBVPV/64-bit",
    "X-Dgi-Req-App": "ggzy-portal",
    # "X-Dgi-Req-Nonce": "xtcz2B8SJLc4FvNO",
    # "X-Dgi-Req-Signature": "7daa204081df92ac1064e8cec1cd36cfe66ebb6575496cc59296e1b97493ccc8",
    # "X-Dgi-Req-Timestamp": "1739271340639",
    "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "_horizon_uid": "5213868e-46b5-4704-8a47-95e551ef9650",
    "_horizon_sid": "c1d9309a-1b1e-4d7f-9bed-5c159f1dfaad"
}
url = "https://ygp.gdzwfw.gov.cn/ggzy-portal/search/v2/items"
data = {
    "type": "trading-type",
    "openConvert": False,
    "keyword": "",
    "siteCode": "44",
    "secondType": "A",
    "tradingProcess": "",
    "thirdType": "[]",
    "projectType": "",
    "publishStartTime": "",
    "publishEndTime": "",
    # "pageNo": 3,
    "pageSize": 10
}
with open('date.csv','a',encoding='utf-8',newline='') as f:
    f_name = ['publishDate','noticeTitle']
    f_data = csv.DictWriter(f, fieldnames=f_name)
    for page in range(1,10):
        data["pageNo"]=page
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        data=json.loads(data)
        items=dict()
        res=response.json()
        for item in res["data"]["pageData"]:
            items["noticeTitle"]=item["noticeTitle"]
            Date=str(item["publishDate"])
            items["publishDate"]=Date[:4]+"-"+Date[4:6]+"-"+Date[6:8]
            f_data.writerow(items)
            print("保存成功")
