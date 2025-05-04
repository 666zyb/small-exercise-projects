import requests
import execjs


class qcc():
    def __init__(self):
        self.url = "https://www.qcc.com/api/home/getNewsFlash"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/105 SLBVPV/64-bit",
        }
        self.params = {
            "firstRankIndex": "1",
            "lastRankIndex": "0",
            "lastRankTime": "",
            "pageSize": "10"
        }
        self.js_code = open('企查查.js', encoding='utf-8').read()
        self.js = execjs.compile(self.js_code)

    def get_data(self):
        response = requests.get(url=self.url, headers=self.headers, params=self.params)
        return response.json()

    def main(self):
        _url = self.url + "?firstRankIndex=&" + "lastRankIndex=" + self.params["lastRankIndex"] + "&lastRankTime=" + \
               self.params["lastRankTime"] + "&pageSize=10"
        ed = self.js.call('get_data', _url)
        self.headers[ed["i"]] = ed["u"]
        data=dict()
        for i in range(1, 20):
            if i != 1:
                self.params = {
                    "firstRankIndex": "",
                    "lastRankIndex": data[-1]["rankIndex"],
                    "lastRankTime": data[-1]["rankIndex"],
                    "pageSize": "10"
                }
            data = self.get_data()
            print(data)


if __name__ == '__main__':
    qc = qcc()
    qc.main()
