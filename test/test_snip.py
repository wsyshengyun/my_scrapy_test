# -*- coding: utf-8 -*-


from test.log import logger
import unittest

logger.info("in snip_test")


class Mytest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_type_name(self):
        obj = A()
        name = type(obj).__name__
        self.assertEqual(name, 'A')

        pass

    def test_dict_pop(self):
        dit = {'a': 1, 'b': 2, 'c': 3}
        value = dit.pop('b')
        self.assertEqual(value, 2)

        pass


class A(object):
    pass


def main():
    pass
