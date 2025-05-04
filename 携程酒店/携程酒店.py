import requests

class XieCheng():
    def __init__(self):
        self.data = {
            "ServerData": "",
            "date": {
                "dateInfo": {
                    "checkInDate": "20250127", # 自己填写日期，不能在之前
                    "checkOutDate": "20250128"
                },
                "dateType": 1,
            },
            "destination": {
                "type": 1,
                "geo": {
                    "cityId": 2,
                    "countryId": 1
                },
                "keyword": {
                    "word": ""
                }
            },
            "hotelIdFilter": {
                "hotelAldyShown": []
            },
            "filters": [
                {
                    "filterId": "29|1",
                    "type": "29",
                    "value": "1|1",
                    "subType": "2"
                }
            ],
            "extraFilter": {
                "childInfoItems": [],
                "sessionId": ""
            },
            "paging": {
                "pageCode": "102002",
                # "pageIndex": 1,
                "pageSize": 10
            },
            "roomQuantity": 1,
            "recommend": {
                "nearbyHotHotel": {}
            },
            "genk": True,
            "head": {
                "platform": "PC",
                "cid": "09031013314543221135",
                "cver": "hotels",
                "bu": "HBU",
                "group": "ctrip",
                "aid": "4897",
                "sid": "130026",
                "ouid": "",
                "locale": "zh-CN",
                "timezone": "8",
                "currency": "CNY",
                "pageId": "102002",
                "vid": "1737192023070.7f49LPPUtaFp",
                "guid": "09031013314543221135",
                "isSSR": False
            },
        }
        self.url = "https://m.ctrip.com/restapi/soa2/31454/json/fetchHotelList"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/105 SLBVPV/64-bit"
        }

    def get_data(self):
        response = requests.post(url=self.url, headers=self.headers, json=self.data)
        return response.json()

    def main(self):
        for page in range(1,10):
            self.data["paging"]["pageIndex"]=page
            print(self.get_data())


if __name__ == '__main__':
    xc = XieCheng()
    xc.main()
