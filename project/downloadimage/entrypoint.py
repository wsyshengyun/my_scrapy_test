from scrapy import cmdline

# cmdline.execute(['scrapy', 'crawl', 'getimage'])
cmdline.execute('scrapy crawl getimage'.split())
