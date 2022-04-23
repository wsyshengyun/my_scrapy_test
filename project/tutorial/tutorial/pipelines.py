# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import logging

# useful for handling different item types with a single interface
import pymongo

logger = logging.getLogger(__name__)


class TutorialPipeline:

    def __init__(self, mongo_host, mongo_port, mongo_db):
        self.mongo_host = mongo_host
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db
        pass

    @classmethod
    def from_crawler(cls, crawler):
        mongo_host = crawler.settings.get('MONGO_HOST')
        mongo_port = crawler.settings.get('MONGO_PORT')
        mongo_db = crawler.settings.get('MONGO_DB')
        return cls(mongo_host, mongo_port, mongo_db)
        pass

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_host, self.mongo_port)
        self.db = self.client[self.mongo_db]
        self.news_collection = self.db['news']

    def close_spider(self, spider):
        self.client.close()
        pass

    def process_item(self, item, spider):
        logger.debug("item is {}".format(item))

        data = {'title': item['title'], 'url': item['url']}
        self.news_collection.insert_one(data)
        return item
