# coding:utf8
import scrapy
from scrapy import Selector

# <?xml version="1.0" encoding="ISO-8859-1"?>
text = \
    """
    <bookstore>
    <book>
      <title lang="chin">Harry Potter</title>
      <price>$29.99元</price>
    </book>
    <book>
      <title lang="eng">Learning XML</title>
      <title lang="bgm at"> XML_</title>
      <title lang="ct bgm at">_XML_</title>
      <title lang="ct bgm">ct is ciry </title>
      <price>$39.95元</price>
    </book>
    <div>
        <p class="testp">nihao00</p>
        <p id=190>nihao01</p>
        <p>nihao02</p>
        <p class="test unit">nihao03</p>
    </div>
    <div class="nihao">
        <p>nihao1</p>
        <p>nihao2</p>
        <p>nihao3</p>
    </div>
    </bookstore>
    """


# print(text)
def test_css():
    """总结 CSS选择器适合选择多个元素,当选择一个元素的时候需要用到伪类选择器,比如p:nth-child(1)"""

    sel = Selector(text=text)
    # id选择器
    #  带空格的类属性选择器
    class_test = sel.css(".test.unit::text")

    result = sel.css("bookstore")
    result1 = sel.css("bookstore book")  # bookstore 的后代 book元素
    result2 = sel.css("bookstore > book")  # 选择 book元素(book元素为bookstores的子元素, 子元素也可能有多个)
    result3 = sel.css("bookstore>title")  # 空的
    result4 = sel.css("bookstore title")  # 两个元素, <title lange ...> <title lange='cng'...>
    result5 = sel.css("bookstore price")
    result51 = sel.css("bookstore price::text")  #
    result6 = sel.css(" [lang='eng']")
    result64 = sel.css(" [lang=eng]")  # 起到引号测试  OK  和reslut6结果是一样的
    result63 = sel.css(" [lang = 'bgm at']")  # 匹配带有空格的属性
    result61 = sel.css(" [lang~= 'bgm']")  # ~ 是测试的 带有空格的属性值,像 bgm at  但是像bgm_at 是不匹配的
    result65 = sel.css(" [lang^= ct]")  # ^ 是以 ct 开头的 标签 2个元素
    result66 = sel.css(" title[lang=eng] + title")  # bgm at
    result62 = sel.css("bookstore [lang='eng']")
    result7 = sel.css("#190")
    result8 = sel.css(".testp")

    # 伪类选择器
    sel_tor1 = sel.css("p:last-child")
    sel_tor2 = sel.css("p:nth-child(2)")
    sel_tor4 = sel.css("p:nth-last-child(2)")
    sel_tor5 = sel.css("p:last-of-type")  # nihao02   nihao3~~~
    sel_tor3 = sel.css("book > :not(title)")

    # 属性值提取器
    attr_get1 = sel.css("title::attr(lang)").extract()
    # attr_get2 = sel.css("attr(lang)").extract()   # 运行不通
    attr_get2 = sel.css("book:nth-child(1)>title::attr(lang)").extract()
    attr_get3 = sel.css("book:nth-child(2)>title::attr(lang)").extract()

    # 标签下文本提取器
    result52 = sel.css("bookstore price::text").re("\d*\.\d*")  # class <list> 类型29.99   39.95
    pass


# test_css()


def test_xpath():
    sel = Selector(text=text)  # 此处必须用关键字来传递参数
    result1 = sel.xpath('//book')
    result2 = sel.xpath('//div')
    result3 = sel.xpath('//title')
    result4 = sel.xpath('//title | //div')
    assert len(result4) == len(result3) + len(result2)

    res1 = sel.xpath("//book[1]")  # 索引从1开始
    res2 = sel.xpath("//book[2]")

    res3 = sel.xpath("/book")  # []
    res3 = sel.xpath("/bookstroe")  # []
    res4 = sel.xpath("/html")  # 正确

    res5 = sel.xpath("//book/title[@lang=eng]").get()  # None
    res6 = sel.xpath("//book//title[@lang='eng']").get()  # 1个元素 Learning XML
    res7 = sel.xpath("//book//title")  # ok 5个元素
    res8 = sel.xpath("//book//title[@lang]")  # ok 5个元素
    res9 = sel.xpath("//book//title[@lang='ct bgm at']")  # 1个元素  注意空格
    res10 = sel.xpath("//book//title[@lang='ct bgm at']/text()").extract()  # 1个元素的文本内容,返回的好像还是一个列表
    res11 = sel.xpath("//book//title[@lang='ct bgm at']/text()").extract_first()  # 1个元素的文本内容,返回的好像还是一个列表

    # 选择标签中得值为xxx的元素
    res12 = sel.xpath("//title[text()=' XML_']")  # 完全等于, 不是包含, XML_前面的空格不能少,少了不匹配
    # 模糊定位
    res13 = sel.xpath("//title[contains(@lang, 'bgm at')]")  # 属性里面包含'bgm at'字符串的被选中

    # . 和  ..
    res14 = sel.xpath("//book[2]")
    res15 = res14.xpath("./title[2]")  # " XML_"
    res16 = res14.xpath("..")  # bookstore标签

    # 所有的文本节点
    res17 = sel.xpath("//book[2]//text()")  # 包含了换行的空元素字符串
    res18 = sel.xpath("//book[2]//text()").extract()  # 包含了换行的空元素字符串

    pass


test_xpath()
