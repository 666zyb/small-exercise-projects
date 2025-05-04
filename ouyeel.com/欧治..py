import requests
from flask import session
from lxml import etree
import execjs
import json



session = requests.session()
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.ouyeel.com",
    "Pragma": "no-cache",
    "Referer": "https://www.ouyeel.com/search-ng/queryResource/index?manufacture=SGJT",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "X-Tingyun-Id": "shNg2wpepqo;r=5239635",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

url = "https://www.ouyeel.com/search-ng/commoditySearch/queryCommodityResult"
response = session.get(url, headers=headers)

# print(response)
html = etree.HTML(response.text)
content = html.xpath('//meta[2]/@content')[0]
ts_code = html.xpath('//script[1]/text()')[0]
with open('new.js', encoding='utf-8') as f:
    js_Code = f.read().replace('content_code',content).replace("'code'",ts_code)
coo = execjs.compile(js_Code).call('getCookie')

cookies = {
    coo.split('=')[0]:coo.split('=')[1],

}

response = requests.get(url, headers=headers, cookies=cookies)
data = {
    "criteriaJson": "{\"pageIndex\":1,\"pageSize\":50,\"industryComponent\":null,\"channel\":null,\"productType\":null,\"sort\":null,\"warehouseCode\":null,\"key_search\":null,\"is_central\":null,\"searchField\":null,\"companyCode\":null,\"inquiryCategory\":null,\"inquirySpec\":null,\"provider\":null,\"packCodes\":null,\"shopCode\":null,\"steelFactory\":null,\"resourceIds\":null,\"jsonParam\":{\"manufacture\":\"SGJT\"},\"excludeShowSoldOut\":null}"
}
response = session.post(url, headers=headers, cookies=cookies, data=data).json()
print(response)
