import requests
import execjs
import json
import time

class yjp():
    def __init__(self):
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip,deflate,br,zstd",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://www.yijiupi.com",
            "Referer": "https://www.yijiupi.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "UUID": "d81c496ad5b9c6d073a45fa8fdb6ad40",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/105 SLBVPV/64-bit",
            "appCode": "ShoppingMallPC",
            "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "token": "",
            # "x-sign": "0bd9360dedf833ac03ac8e78fa6e9a0d624b5100",
            # "x-sign-nonce": "ce2e7787_4d88_48c9_8c6a_321bcf91f0c3",
            # "x-sign-timestamp": "1739351224",
            "x-sign-version": "1.0"
        }
        self.url = "https://www.yijiupi.com/v58/Product/List"
        self.data = {
            "currentPage": 2,
            "data": {
                "brandIds": [
                    "3684"
                ],
                "searchModes": [
                    2
                ],
                "sort": 0,
                "currentPage": 2,
                "pageSize": 25,
                "filterSpecialArea": False,
                "searchSource": 1,
                "searchKeyNotCorrect": False,
                "hidBottomBar": False,
                "brandId": ""
            },
            "pageSize": 25,
            "cityId": 402,
            "countyRegionId": "320116",
            "userClassId": 1,
            "userDisplayClass": 0,
            "addressId": "",
            "deviceType": 3
        }

        self.js_code = open('易久批.js', encoding='utf-8').read()
        self.js = execjs.compile(self.js_code)

    def get_data(self, data):
        response = requests.post(self.url, headers=self.headers, data=data)
        print(response)
        return response.text

    def main(self):
        xxx = json.dumps(self.data, separators=(',', ':'))
        ed = self.js.call('zyb', None,xxx)
        self.headers["X-Sign"] = ed["sign"]
        self.headers["X-Sign-Nonce"] = ed["nonce"]
        self.headers["X-Sign-Timestamp"] = ed["timestamp"]
        print(self.headers)
        data = self.get_data(xxx)
        print(data)


if __name__ == '__main__':
    z = yjp()
    z.main()
