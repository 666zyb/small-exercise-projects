import scrapy
from scrapy import cmdline
import re

class WangzheheroimageSpider(scrapy.Spider):
    name = "wangzheHeroImage"
    allowed_domains = ["pvp.qq.com","game.gtimg.cn"]
    start_urls = ["https://pvp.qq.com/web201605/js/herolist.json","https://pvp.qq.com/ip/skin.html"]

    def parse(self, response):
        for item in response.json():
            hero_name=item['cname']
            hero_ename=item['ename']
            yield {
                'type':"info",
                'hero_name':hero_name
            }
            try:
                hero_image_url = item['m_bl_link']
                if "https:" not in hero_image_url:
                    hero_image_url="https:"+hero_image_url
            except KeyError:
                hero_image_url = f"https://pvp.qq.com/web201605/herodetail/{hero_ename}.shtml"

            yield scrapy.Request(url=hero_image_url,callback=self.parse_image,cb_kwargs={'hero_name':hero_name})

    def parse_image(self,response,hero_name):
        try:
            res=response.xpath('//div[@class="zk-con1 zk-con"]/@style')[0]
            pattern = re.compile(r"(\/.*g)")
            # 使用 search 方法查找匹配的 url
            match = pattern.search(str(res))
            url="https:"+match.group(0)
        except IndexError:
            res=response.xpath('//div[@class="main-bg-height portrait"]/img/@src')[0]
            url="https:"+str(res)
        yield {
            'type':'url',
            'url':url
        }
        yield scrapy.Request(url=url, callback=self.parse_hero_image, cb_kwargs={'hero_name':hero_name})

    def parse_hero_image(self,response,hero_name):
        yield {
            'type':'hero_image',
            'filename': hero_name + '.png',
            'image_content': response.body
        }

if __name__=='__main__':
    cmdline.execute('scrapy crawl wangzheHeroImage'.split())