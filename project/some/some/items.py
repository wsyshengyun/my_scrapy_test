# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()  # 书名
    price = scrapy.Field()   # 价格
    stock_num = scrapy.Field()  # 库存
    reviews_num = scrapy.Field()  # 评论
    description = scrapy.Field()  # 描述

    pass
