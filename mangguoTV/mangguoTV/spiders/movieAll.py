import scrapy
from scrapy import cmdline


class MovieallSpider(scrapy.Spider):
    name = "movieAll"
    allowed_domains = ["pianku.api.mgtv.com","hitv.com"]
    start_urls = ["https://pianku.api.mgtv.com/rider/list/pcweb/v3?allowedRC=1&platform=pcweb&channelId=3&pn=1&pc=80&hudong=1&_support=10000000&kind=a1&edition=a1&area=a1&year=all&chargeInfo=a1&sort=c2"]

    def start_requests(self):
        for pn in range(1,10):
            url=f"https://pianku.api.mgtv.com/rider/list/pcweb/v3?allowedRC=1&platform=pcweb&channelId=3&pn={pn}&pc=80&hudong=1&_support=10000000&kind=a1&edition=a1&area=a1&year=all&chargeInfo=a1&sort=c2"
            yield scrapy.Request(url)

    def parse(self, response):
        res=response.json()
        for items in res["data"]["hitDocs"]:
            title=items["title"]
            image_url=items["img"]
            actors=items["subtitle"]

            yield {
                'type':'info',
                'title':title,
                'image_url':image_url,
                'actors':actors
            }

            yield scrapy.Request(url=image_url,callback=self.parse_image,cb_kwargs={"name":title})

    def parse_image(self,response,name):
        yield {
            'type':'image',
            'title':name,
            'file_name':name+".png",
            'image_content':response.body
        }


if __name__=="__main__":
    cmdline.execute('scrapy crawl movieAll --loglevel=WARNING'.split())
