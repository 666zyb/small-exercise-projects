# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QingtingfmPipeline:
    def process_item(self, item, spider):
        with open('qingting.csv','a',encoding='utf-8',newline='') as f:
            f_name=['badge','cover_url','title']
            f_book=csv.DictWriter(f,fieldnames=f_name)
            f_book.writeheader()
            f_book.writerow(item)
