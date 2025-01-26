import scrapy
from scrapy import cmdline


class TxWorkSpider(scrapy.Spider):
    name = "tx_Work"
    allowed_domains = ["careers.tencent.com"]
    # start_urls = ["https://careers.tencent.com/search.html?query=at_1"]

    def start_requests(self):
        url='https://careers.tencent.com/search.html?index={}&keyword=python'
        for page in range(1,33):
            yield scrapy.Request(url=url.format(page))

    def parse(self, response,**kwargs):
        div_list=response.xpath("//div[@class='correlation-degree']/div/div")
        for div in div_list:
            item=dict()
            item['title']=div.xpath('./a//span[@class="job-recruit-title"]/text()').extract_first()
            item['department']=div.xpath('./a/p[1]/span[1]/text()').extract_first()
            item['address']=div.xpath('./a//span[2]/text()').extract_first()
            item['post']=div.xpath('./a/p[1]/span[3]/text()').extract_first()
            item['date']=div.xpath('./a/p[1]/span[last()]/text()').extract_first()
            item['recruit-data']=div.xpath('./a/p[2]/text()').extract_first()
            yield item


if __name__=="__main__":
    cmdline.execute('scrapy crawl tx_Work'.split())
