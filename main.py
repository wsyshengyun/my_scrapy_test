# -*- coding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2022/04/01 07:23:47

'''
from test.log import logger

logger.info("-" * 100)

import unittest

# from test.snip_test import main


# main()


# def run_test():
s = unittest.TestSuite()
loader = unittest.TestLoader()

path = 'test/'
s.addTests(loader.discover(path))

run = unittest.TextTestRunner()
run.run(s)

# run_test()
