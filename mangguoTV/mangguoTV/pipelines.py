# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MangguotvPipeline:
    def __init__(self):
        self.csv_file_created = False

    def process_item(self, item, spider):
        if item.get('type')=='info':
            with open('movieAll.csv','a',encoding='utf-8',newline='') as f:
                f_name=['title','image_url','actors']
                f_movies=csv.DictWriter(f,fieldnames=f_name)
                if not self.csv_file_created:  # 仅在第一次时写入表头
                    f_movies.writeheader()
                    self.csv_file_created = True
                items=dict()
                items['title']=item.get('title')
                items['image_url']=item.get('image_url')
                items['actors']=item.get('actors')
                f_movies.writerow(items)
                print('保存成功'+item.get('title'))

        elif item.get('type')=='image':
            path=os.getcwd()+'/image/'
            if not os.path.exists(path):
                os.mkdir(path)
            with open(path+item.get('file_name'),'wb') as f:
                f.write(item.get('image_content'))
                print("下载成功"+item.get('title'))

        else:
            print('类型不符合')