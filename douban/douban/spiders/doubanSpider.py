import requests
import scrapy
from scrapy import cmdline

class DoubanspiderSpider(scrapy.Spider):
    name = "doubanSpider"
    allowed_domains = ["movie.douban.com","doubanio.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        res=response.xpath('//div[@class="item"]')
        for item in res:
            title=item.xpath('./div[@class="info"]/div[@class="hd"]/a/span[1]/text()').extract_first()
            image_url=item.xpath('./div[@class="pic"]/a/img/@src').extract_first()
            count=item.xpath('./div[@class="info"]/div[@class="bd"]/div/span[last()]/text()').extract_first()
            yield {
                'type':'info',
                'title':title,
                'image_url':image_url,
                'count':count
            }

            yield scrapy.Request(url=image_url,callback=self.parse_image,cb_kwargs={'image_name':title})

            #翻页
            if response.xpath('//span[@class="next"]/a/@href'):
                next_url=response.urljoin(response.xpath('//span[@class="next"]/a/@href').extract_first())
                yield scrapy.Request(url=next_url,callback=self.parse)
            else:
                print("没有下一页了")

    def parse_image(self,response,image_name):
        yield {
            'type':'image',
            'filename':image_name+'.png',
            'image_content':response.body
        }





if __name__=="__main__":
    cmdline.execute('scrapy crawl doubanSpider --loglevel=WARNING'.split())