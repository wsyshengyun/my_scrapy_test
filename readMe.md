
## 安装

pip安装  
pip需要19以上的版本

## 开始

tutorial/: 该项目的总模块
tutorial/items.py :项目的item文件,编写爬取的字段名称等;
tutorial/pipelines.py : 项目中的pipelines文件; 
tutorial/settings.py  项目的设置文件,较为重要 
tutorial/spiders/  放置spider代码的主目录

大批量的分布式的爬取  采用Redis数据库, 可安装scrapy-reids,用redis数据库来替换scrapy原来使用的队列结构.并配合其他数据库存储.


涉及代理
Headers头中间请求信息处理的时候,使用中间件Middleware来实现.Spider中间件是介入到Scrapy的Spider处理机制的钩子框架.

掌握settings的各种设置

重新定义def start_requests(self)函数来加载cookie信息.

采用scrapy+phantomJS
downloadMiddleware对从scheduler送来的Request对象在请求之前进行预处理,可以实现添加headers, user_agent,还有cookie等功能.


