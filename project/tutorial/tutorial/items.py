# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
""" 
项目的Item文件,编写爬取的字段名称等.
"""
from scrapy import Field
import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NewItem(scrapy.Item):
    title = scrapy.Field() 
    url = scrapy.Field() 

    
class Example(scrapy.Item):
    x = Field(a='hello', b=[1,2,3])
    y = Field(a = lambda x:x**2) 
    

