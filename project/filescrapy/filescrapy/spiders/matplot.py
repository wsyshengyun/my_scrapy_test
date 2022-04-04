import scrapy


class MatplotSpider(scrapy.Spider):
    name = 'matplot'
    allowed_domains = ['matplotlib.org']
    start_urls = ['http://matplotlib.org/examples/index.html']

    def parse(self, response):
        pass
