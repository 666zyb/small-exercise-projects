import scrapy
from scrapy import cmdline


class QingtingSpider(scrapy.Spider):
    name = "qingting"
    allowed_domains = ["m.qingting.fm"]
    start_urls = ["https://m.qingting.fm/rank/"]

    def parse(self, response):
        rsl=response.xpath('//div[@class="rank-list"]/a')
        for item in rsl:
            badge=item.xpath('./div[@class="badge"]/text()').extract_first()
            cover_url=item.xpath('./img/@src').extract_first()
            title=item.xpath('./div[@class="content"]/div[@class="title"]/text()').extract_first()

            yield {
                "badge":badge,
                "cover_url":cover_url,
                "title":title
            }
            print(badge,cover_url,title)

if __name__=="__main__":
    cmdline.execute('scrapy crawl qingting'.split())