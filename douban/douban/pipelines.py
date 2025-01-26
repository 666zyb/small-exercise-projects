# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubanPipeline:
    def __init__(self):
        self.csv_file_created = False

    def process_item(self, item, spider):
        type_=item.get('type')
        if type_=='info':
            with open('douban.csv','a',encoding='utf-8',newline='') as f:
                f_name=['title','image_url','count']
                f_douban=csv.DictWriter(f,fieldnames=f_name)
                if not self.csv_file_created:  # 仅在第一次时写入表头
                    f_douban.writeheader()
                    self.csv_file_created = True
                items=dict()
                items['title']=item.get('title')
                items['image_url']=item.get('image_url')
                items['count']=item.get('count')
                f_douban.writerow(items)
                print('保存成功')

        elif type_=='image':
            now_path=os.getcwd()+'/image/'
            if not os.path.exists(now_path):
                os.mkdir(now_path)
            with open(now_path+item.get("filename"),'wb') as f:
                f.write(item.get('image_content'))
                print("下载完成"+item.get('filename'))
        else:
            print("类型不符合")
