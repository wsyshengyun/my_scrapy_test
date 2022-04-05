import scrapy
from scrapy.http import Response
from some.items import BookItem
from scrapy.linkextractors import LinkExtractor

class BasicSpider(scrapy.Spider):
    name = 'basic'
    # allowed_domains = ['toscrape.com']
    start_urls = ['http://books.toscrape.com/index.html']
    max_count = 2
    
    def __init__(self ):
        self.num = 0
        pass
        
        

    def parse(self, response):

        le = LinkExtractor(restrict_css='article.product_pod h3')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_book)
        
        # 提取下一页
        le = LinkExtractor(restrict_css='ul.pager li.next') 
        links = le.extract_links(response=response)
        if links and self.num<self.max_count:
            next_url = links[0].url 
            self.num+= 1
            yield scrapy.Request(next_url, callback=self.parse)
        

        pass

    
    def parse_book(self, response:Response):
        
        sel = response.selector
        item = BookItem() 
        item['book_name' ]= sel.xpath('//h1/text()').get()
        item['price' ]= sel.xpath('//h1/../p/text()').re('\d+\.\d*')[0]
        
        item['stock_num' ]= sel.xpath('//table[@class="table table-striped"]//tr[6]/td/text()' ).re('\d+')[0]
        item['reviews_num' ]= sel.xpath('//table[@class="table table-striped"]//tr[7]/td/text()').get()
        item['description' ]= sel.xpath('//*[@id="content_inner"]/article/p/text()').get()
        return item
        pass
