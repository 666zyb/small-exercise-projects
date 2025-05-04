import time

import requests
import execjs


class SouSuo33():
    def __init__(self):
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Origin": "https://fse.agilestudio.cn",
            "Pragma": "no-cache",
            "Referer": "https://fse.agilestudio.cn/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/105 SLBVPV/64-bit",
            # "X-Signature": "6c4dcad7bb0b3d029d3aed991ec4b9ec",
            "^sec-ch-ua": "^\\^Chromium^^;v=^\\^9^^, ^\\^Not?A_Brand^^;v=^\\^8^^^",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^"
        }
        self.url = "https://fse-api.agilestudio.cn/api/search"
        self.params = {
            "keyword": "火车呼啸而过",
            "page": "2",
            "limit": "12",
            "_platform": "web",
            "_versioin": "0.2.5",
            "_ts": "1737615196506"
        }
        self.js_code = open('33搜帧.js', encoding='utf-8').read()
        self.js = execjs.compile(self.js_code)

    def get_data(self):
        Signature = self.js.call('zyb', self.params)
        self.headers["X-Signature"] = Signature["sign"]
        self.params["_ts"] = Signature["time"]
        # 注意：这里的时间戳不能用time.time()来生成，因为在网页的js代码中对时间戳进行了修改，所以需要用js代码中修改之后的时间戳才可以，否则
        #      会出现签名错误
        response = requests.get(url=self.url, headers=self.headers,params=self.params)
        return response.json()

    def main(self):
        data = self.get_data()
        print(data)


if __name__ == '__main__':
    ss = SouSuo33()
    ss.main()
