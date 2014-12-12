# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SaveEntriesPipeline(object):
    def process_item(self, item, spider):
        out = open('entries.txt','a') 
        for each in item['MAID']:
          out.write(str(item['CTID']) + "," + str(item['CPID']) + "," + str(each[2]) + "\n") 
        out.close()
               
