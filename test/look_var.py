# coding:utf8
"""
查看调试的时候一些变量类型的符号
"""

dit = dict(a=1, b=2)
lit = list([1, 2, 3])
a = 2


class A:
    def __init__(self, a=1, b=2):
        """ """
        self.a = a
        self.b = b

    def __str__(self):
        return 'nihao'


obja = A()
tsr = "1, 2, 3"
import datetime

today = datetime.datetime.today()


class B:
    c = 1

    def __init__(self, a=2):
        """ """
        self.a = a
        print("is init, a is {}".format(self.a))

    @classmethod
    def foo(cls):
        return cls(5)


B.foo()
