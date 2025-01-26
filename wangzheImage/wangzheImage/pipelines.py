# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WangzheimagePipeline:
    def process_item(self, item, spider):
        if spider.name=='wangzheHeroImage':
            if item.get('type')=='hero_image':
                path_now = os.getcwd() + '/hero_image/'
                if not os.path.exists(path_now):
                    os.mkdir(path_now)
                with open(path_now + item.get('filename'), 'wb') as f:
                    f.write(item.get('image_content'))
        else:
            return item
class WangzhepifuimagePipeline:
    def process_item(self, item, spider):
        if spider.name == 'WangzheHeropifuImageSpider':
            if item.get('type')=='pifu_image':
                path_now = os.getcwd() + '/pifu_image/'
                if not os.path.exists(path_now):
                    os.mkdir(path_now)
                with open(path_now + item.get('file_name'), 'wb') as f:
                    f.write(item.get('image_content'))