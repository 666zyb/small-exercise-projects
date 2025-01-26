import requests
import scrapy
from scrapy import cmdline


class WangzheHeropifuImageSpider(scrapy.Spider):
    name = "WangzheHeropifuImageSpider"
    allowed_domains = ["pvp.qq.com", "game.gtimg.cn"]
    start_urls =["https://pvp.qq.com/zlkdatasys/yuzhouzhan/pfjs.json?t=1735362270017"]

    def parse(self, response):
        res=response.json()['pflbzt_8051']
        for item in res:
            pifu_url="https:"+item['pffmyz_1384']
            pifu_name=item['pfjsbt_2624']
            hero_name=item['pfjstc_2911']
            yield {
                'type':'info',
                'pifu_url':pifu_url,
                'pifu_name':pifu_name,
                'hero_name':hero_name
            }

            yield scrapy.Request(url=pifu_url,callback=self.parse_image,cb_kwargs={'pifu_name':pifu_name,'hero_name':hero_name})


    def parse_image(self,response,pifu_name,hero_name):
        yield {
            'type':'pifu_image',
            'file_name':pifu_name+'-'+hero_name+'.jpg',
            'image_content':response.body
        }


if __name__=='__main__':
    cmdline.execute('scrapy crawl WangzheHeropifuImageSpider'.split())