import requests


class XieCheng():
    def __init__(self):
        self.data = {
            "partner_id": "web",
            # "timestamp": 1737544523332,
            "param": {
                "subnavType": 1,
                "subnavNick": "web_news",
                "pageSize": 30,
                "pageEvent": 1,
                "pageCallback": "eyJmaXJzdElkIjo0ODM0MTYwLCJsYXN0SWQiOjQ4MzQwMTcsImZpcnN0Q3JlYXRlVGltZSI6MTczNzYwNTIyODk3MSwibGFzdENyZWF0ZVRpbWUiOjE3Mzc1OTkxNTQ0OTd9",
                "siteId": 1,
                "platformId": 2
            }
        }
        self.url = "https://gateway.36kr.com/api/mis/nav/ifm/subNav/flow"
        self.headers = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "^Cookie": "Hm_lvt_713123c60a0e86982326bae1a51083e1=1737541674; HMACCOUNT=6B3DD5184F6958B7; Hm_lvt_1684191ccae0314c6254306a8333d090=1737541674; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=^%^7B^%^22distinct_id^%^22^%^3A^%^221948d8de5f286a-05623ef289df0b-27b4036-921600-1948d8de5f36a5^%^22^%^2C^%^22^%^24device_id^%^22^%^3A^%^221948d8de5f286a-05623ef289df0b-27b4036-921600-1948d8de5f36a5^%^22^%^2C^%^22props^%^22^%^3A^%^7B^%^22^%^24latest_traffic_source_type^%^22^%^3A^%^22^%^E7^%^9B^%^B4^%^E6^%^8E^%^A5^%^E6^%^B5^%^81^%^E9^%^87^%^8F^%^22^%^2C^%^22^%^24latest_referrer^%^22^%^3A^%^22^%^22^%^2C^%^22^%^24latest_referrer_host^%^22^%^3A^%^22^%^22^%^2C^%^22^%^24latest_search_keyword^%^22^%^3A^%^22^%^E6^%^9C^%^AA^%^E5^%^8F^%^96^%^E5^%^88^%^B0^%^E5^%^80^%^BC_^%^E7^%^9B^%^B4^%^E6^%^8E^%^A5^%^E6^%^89^%^93^%^E5^%^BC^%^80^%^22^%^7D^%^7D; Hm_lpvt_1684191ccae0314c6254306a8333d090=1737544084; Hm_lpvt_713123c60a0e86982326bae1a51083e1=1737544084^",
            "Origin": "https://36kr.com",
            "Pragma": "no-cache",
            "Referer": "https://36kr.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/105 SLBVPV/64-bit",
            "^sec-ch-ua": "^\\^Chromium^^;v=^\\^9^^, ^\\^Not?A_Brand^^;v=^\\^8^^^",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^"
        }

    def get_data(self):
        response = requests.post(url=self.url, headers=self.headers, json=self.data)
        return response.json()

    def main(self):
        for page in range(1, 10):
            res=self.get_data()
            pageCallback=res["data"]["pageCallback"]
            self.data["param"]["pageCallback"] = pageCallback
            print(self.get_data())
            print(pageCallback)


if __name__ == '__main__':
    xc = XieCheng()
    xc.main()
