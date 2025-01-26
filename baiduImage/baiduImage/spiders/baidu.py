"""
   爬取百度二次元大全图片
   爬取的URL地址:’https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2
                &lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1735311690693_R&pv=&ic=
                &nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0
                &istype=2&dyTabStr=MCwzLDEsMiwxMyw3LDYsNSwxMiw5&ie=utf-8
                &sid=&word=%E4%BA%8C%E6%AC%A1%E5%85%83%E5%A4%A7%E5%85%A8‘
   字段包括：
   - title: 二次元图片名称
   - image_url: 二次元图片URL

   将字段信息保存在(二次元.csv)文件
   下载二次元图片到image文件夹
"""

import scrapy
from scrapy import cmdline
import json
import re

class BaiduSpider(scrapy.Spider):
    count=0
    name = "baidu"
    allowed_domains = ["image.baidu.com","baidu.com"]
    # start_urls = ["https://image.baidu.com/search/index"]

    def start_requests(self):
        url='https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8049085011589270997&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E4%BA%8C%E6%AC%A1%E5%85%83%E5%A4%A7%E5%85%A8&queryWord=%E4%BA%8C%E6%AC%A1%E5%85%83%E5%A4%A7%E5%85%A8&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={}&rn=30&gsm={}&1735205089723='
        for page in range(1,10):
            pn=hex(page*30)[2:]
            yield scrapy.Request(url=url.format(page*30,pn))

    def parse(self, response):
        try:
            text = response.json()
        except json.JSONDecodeError:
            text=re.sub(r"\\'",'0',response.text)
            text=json.loads(text)
        for items in text['data']:
            title=items['fromPageTitle']
            image_url=items['hoverURL']
            self.count+=1
            yield {
                'type':'info',
                'title':title,
                'image_url':image_url
            }
            if "http" not in image_url:
                image_url='https://'+image_url
            yield scrapy.Request(url=image_url,callback=self.parse_image,cb_kwargs={'name':title,'count':self.count})


    def parse_image(self,response,name,count):
        filename=name+'.jpg'
        yield {
            'type':'image',
            'filename':filename,
            'image_content':response.body,
            'count':count
        }


if __name__=='__main__':
    cmdline.execute('scrapy crawl baidu --loglevel=WARNING'.split())