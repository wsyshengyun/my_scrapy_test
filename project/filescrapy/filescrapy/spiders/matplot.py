import scrapy
from scrapy.linkextractors import LinkExtractor
from filescrapy.items import FilescrapyItem

class MatplotSpider(scrapy.Spider):
    name = 'matplot'
    allowed_domains = ['matplotlib.org']
    start_urls = ['http://matplotlib.org/examples/index.html']

    def parse(self, response):
        
        le = LinkExtractor(restrict_css='div.toctree-wrapper.compound', deny='/index.html$')
        for link in le.extract_links(response):
            yield scrapy.Request(url = link.url, callback=self.parse_example)
        pass

    
    def parse_example(self, response):
        
        href = response.css('a.reference.external::attr(href)').extract_first() 
        url = response.urljoin(href)
        example = FilescrapyItem() 
        example['file_urls'] = [url]
        yield example
        pass
        
        
