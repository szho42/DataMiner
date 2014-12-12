# -*- coding: utf-8 -*-
import pickle
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SaveEntriesPipeline(object):
    def process_item(self, item, spider):
        out = open('entries','wb') 
        pickle.dump(item,out)
