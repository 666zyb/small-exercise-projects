import requests
import execjs


class qimai():
    def __init__(self):
        self.url = "https://api.qimai.cn/indexV2/getIndexRank"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/105 SLBVPV/64-bit",
        }
        self.params = {
            "setting": "0",
            "genre": "5000^"
        }
        self.js_code=open('七麦.js', encoding='utf-8').read()
        self.js=execjs.compile(self.js_code)
        self.a=list(self.params.values())

    def get_data(self):
        response=requests.get(url=self.url,headers=self.headers,params=self.params)
        return response.json()


    def main(self):
        analysis=self.js.call('zyb',self.a)
        self.params["analysis"]=analysis
        res=self.get_data()
        print(res)

if __name__ == '__main__':
    qm=qimai()
    qm.main()
