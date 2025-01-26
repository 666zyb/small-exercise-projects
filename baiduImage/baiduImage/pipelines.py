# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BaiduImagePipeline:
    def __init__(self):
        self.csv_file_created = False

    def process_item(self, item, spider):
        type_ = item.get('type')
        if type_ == 'info':
            with open('二次元.csv', 'a', encoding='utf-8', newline='') as f:
                f_name = ['title', 'image_url']
                f_image = csv.DictWriter(f, fieldnames=f_name)
                if not self.csv_file_created:
                    f_image.writeheader()
                    self.csv_file_created = True
                items=dict()
                items['title']=item.get('title')
                items['image_url']=item.get('image_url')
                f_image.writerow(items)
                print('数据保存成功', item.get('title'))

        elif type_ == 'image':
            now_path = os.getcwd() + '/image/'
            if not os.path.exists(now_path):
                os.mkdir(now_path)
            with open(now_path + str(item.get('count'))+'.jpg', 'wb') as f:
                f.write(item.get("image_content"))
                print('图片下载成功', item.get('filename').split(sep='.')[0])
