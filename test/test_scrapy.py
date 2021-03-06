from select import select
from unittest import result
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import unittest
from test.log import logger

body = '''
 <html>
    <body>
        <h1>Hello World</h1>
        <h2>Hello Scrapy</h2>
        <b>Hello python</b>
        <ul>
           <li>C++<li>llll</li></li>
           <li>Java<a @href='www'>666</a></li>
           <li #2312>Python</li>
           <li>Python</li>
        </ul>
    </body>
 </html>
 '''

class MyScrapyTest(unittest.TestCase):
     
    def setUp(self) -> None:
        self.response = HtmlResponse(url='http://www.example.com', body=body, encoding='utf8')
        self.selector = Selector(response=self.response)
        
        self.text = '''
            <ul>
                <li>python学习手册<b>价格: 99.00元</b></li> 
                <li>python核心编程 <b>价格: 88.00元</b></li> 
                <li>python基础教程<b>价格: 80.00元></b></li> 
            </ul> 
        '''

    def tearDown(self) -> None:
        return super().tearDown()

        
    def test_1(self):
        
        logger.info("response url is {}".format(self.response.url))

        selector_list = self.selector.xpath('//h1')
        logger.info("selector_list is {}".format(selector_list))

        for sel in selector_list:
            logger.info("{}".format(sel.xpath('./text()').get()))
            logger.info("{}".format(sel.xpath('./text()').extract()))
            logger.info("{}".format(sel.xpath('./text()').extract_first()))
        pass

    
    def test_xpath_re(self):
        
        selector = Selector(text = self.text) 
        # result = selector.xpath('.//li/b')
        result = selector.xpath('.//li/b/text()').re('\d+\.\d+')
        logger.info("result is {}".format(result))
        pass

    
    def test_response(self):
        
        selector = Selector(text = body)
        selector2 = self.response.selector

        # logger.info("selector = {}".format(selector))
        # logger.info("selector2 = {}".format(selector2))

        pass
        
    
    
    def test_css(self):
        
        a1 = self.selector.css('h1,b')
        logger.info(" a1 各个{}".format(a1))

        # TODO 后代和子是一样的
        a2 = self.selector.css('ul li')
        logger.info(" a2 后代{}".format(a2))

        a3 = self.selector.css('ul>li')
        logger.info("a3 子  {}".format(a3))

        
        # self.assertEqual(a2, a3)

        
        a4 = self.selector.css('h1 + h2')
        logger.info("a4 兄弟 {}".format(a4))

        
        a5 = self.selector.css('#2312')
        logger.info("a5 = {}".format(a5))
        
        pass
        
        
         
    
