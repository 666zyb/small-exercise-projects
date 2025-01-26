# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TxworkPipeline:
    def __init__(self):
        self.csv_file_created = False

    def process_item(self, item, spider):
        with open('txWork.csv','a',encoding='utf-8',newline='') as f:
            f_name=['title','department','address','post','date','recruit-data']
            f_work=csv.DictWriter(f,fieldnames=f_name)
            if not self.csv_file_created:  # 仅在第一次时写入表头
                f_work.writeheader()
                self.csv_file_created = True
            f_work.writerow(item)
