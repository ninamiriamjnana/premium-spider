# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PspiderPipeline(object):
    def process_item(self, item, spider):
        return item


# example here http://stackoverflow.com/questions/10845839/writing-items-to-a-mysql-database-in-scrapy
