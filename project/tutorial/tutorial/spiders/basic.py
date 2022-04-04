import scrapy
from tutorial.items import NewItem

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['baidu.com']
    start_urls = ['http://news.baidu.com/']

    def parse(self, response):

        for i in range(1,5):
            url = response.xpath('//*[@id="pane-news"]/div/ul/li[%d]/strong/a/@href' % i).get()
            title = response.xpath('//*[@id="pane-news"]/div/ul/li[%d]/strong/a/text()' % i).get()
            item = NewItem()
            item[title] = title
            item['url'] = url 
            yield item


        
