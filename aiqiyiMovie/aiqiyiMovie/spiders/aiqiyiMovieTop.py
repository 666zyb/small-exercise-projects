"""
   爬取爱奇艺电影
   爬取的URL地址:https://www.iqiyi.com/movie/
   字段包括：
   - movie_name: 电影名称
   - sns_score: 电影评分
   - movie_cover_url: 电影封面图片URL
   - movie_video_url: 电影视频URL

   将字段信息保存在movie.csv文件
   下载电影封面图片到image文件夹
"""

import scrapy
from scrapy import cmdline

class AiqiyimovietopSpider(scrapy.Spider):
    name = "aiqiyiMovieTop"
    allowed_domains = ["www.iqiyi.com","mesh.if.iqiyi.com","iqiyipic.com"]
    start_urls = ["https://www.iqiyi.com/movie/"]

    def start_requests(self):
        url='https://mesh.if.iqiyi.com/portal/lw/videolib/data?uid=&passport_id=&ret_num=60&version=12.123.20834&device_id=e6b27cd491199ce71449385f788c4e4e&channel_id=1&page_id={}&session=8ffd9866e7d33b367c36c665d0e91f1d&os=&conduit_id=&vip=0&auth=&recent_selected_tag=%E9%AB%98%E5%88%86&ad=%5B%7B%22lm%22%3A%225%22%2C%22ai%22%3A%225%22%2C%22fp%22%3A%226%22%2C%22sei%22%3A%22S00c596ee321943edab98a61d933a2e31%22%2C%22position%22%3A%22library%22%7D%5D&adExt=%7B%22r%22%3A%221.2.1-ares6-pure%22%7D&dfp=a00f54739fdf0440cb8f76427d1cad7dc75bbfffe61929901bb7e3dbd33d746cff&filter=%7B%22mode%22%3A%228%22%7D'
        for page_id in range(1,10):
            yield scrapy.Request(url=url.format(page_id))

    def parse(self, response):
        for item in response.json()['data']:
            movie_name=item['display_name']
            movie_cover_url=item['image_cover']
            movie_video_url=item['page_url']
            sns_score=item.get('sns_score',None)
            # 或者:
            # try:
            #     sns_score=item['sns_score']
            # except KeyError:
            #     sns_score=None
            yield {
                'type':'info',
                'movie_name':movie_name,
                'movie_cover_url':movie_cover_url,
                'movie_video_url':movie_video_url,
                'sns_score':sns_score
            }

            yield scrapy.Request(movie_cover_url,callback=self.parse_image,cb_kwargs={'movie_name':movie_name})


    def parse_image(self,response,movie_name):
        yield {
            'type':'image',
            'filename':movie_name+'.jpg',
            'image_content':response.body
        }



if __name__=="__main__":
    cmdline.execute("scrapy crawl aiqiyiMovieTop".split())