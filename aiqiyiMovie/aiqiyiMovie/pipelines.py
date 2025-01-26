# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AiqiyimoviePipeline:
    def __init__(self):
        self.a=False

    def process_item(self, item, spider):
        if item.get('type')=='info':
            with open('movie.csv','a',encoding='utf-8',newline='') as f:
                f_name=['movie_name','sns_score','movie_cover_url','movie_video_url']
                f_video=csv.DictWriter(f,fieldnames=f_name)
                if not self.a:
                    f_video.writeheader()
                    self.a=True
                items=dict()
                items['movie_name']=item.get('movie_name')
                items['sns_score'] = item.get('sns_score')
                items['movie_cover_url'] = item.get('movie_cover_url')
                items['movie_video_url'] = item.get('movie_video_url')
                f_video.writerow(items)

        if item.get('type')=='image':
            path_now=os.getcwd()+'/image/'
            if not os.path.exists(path_now):
                os.mkdir(path_now)
            with open(path_now+item.get('filename'),'wb') as f:
                f.write(item.get('image_content'))