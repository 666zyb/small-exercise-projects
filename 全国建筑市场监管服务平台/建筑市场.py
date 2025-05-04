import requests
import execjs

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/105 SLBVPV/64-bit",
    "^sec-ch-ua": "^\\^Chromium^^;v=^\\^9^^, ^\\^Not?A_Brand^^;v=^\\^8^^^",
    "sec-ch-ua-mobile": "?0",
    "^sec-ch-ua-platform": "^\\^Windows^^^",
    "Referer": "https://jzsc.mohurd.gov.cn/",
    "Referer;": "",
    "Purpose": "prefetch",
    "accept": "text/css,*/*;q=0.1",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0",
    "referer": "https://jzsc.mohurd.gov.cn/",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/105 SLBVPV/64-bit",
    "cookie": "H_WISE_SIDS_BFESS=61027_61217_60853_61491_61506_61496_61531_61637_61694; BAIDUID_BFESS=3018F958B3325A9AA68EFEA829B9A667:FG=1; ZFY=5eg2nXc0Df4Ft8duwMV3lq5X3vrtHSer:AZo6P1Z6:Ad0:C",
    "Origin": "https://jzsc.mohurd.gov.cn",
    "origin": "https://jzsc.mohurd.gov.cn",
    "accessToken;": "",
    "timeout": "30000",
    "v": "231012"
}
cookies = {
    "Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c": "1736932408,1737435346",
    "HMACCOUNT": "6B3DD5184F6958B7",
    "Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c": "1737444781"
}
url = "https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list"
js = execjs.compile(open('建筑市场.js', encoding='utf-8').read())
for pg in range(1, 10):
    params = {
        "pg": pg,
        "pgsz": "15",
        "total": "450"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    res = js.call('parse_data', response.text)
    print(res)
