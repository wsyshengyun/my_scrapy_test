# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

# class FilescrapyPipeline:
# def process_item(self, item, spider):
# return item


# class MyFilesPipeline(FilesPipeline):

#     def file_path(self, request, response=None, info=None, *, item=None):
#         # return super().file_path(request, response, info, item=item)
#         path = urlparse(request.url).path 
#         return join(basename(dirname(path)), basename(path))
