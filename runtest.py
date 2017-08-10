#! python2
# coding: utf-8

from package.HTMLTestRunner import HTMLTestRunner
import unittest
import time
import os

# 指定测试用例目录
cases_dir = './testcases'

# discover()方法可以自动查找指定目录（cases_dir）下指定文件名（test_*.py）里面的测试用例，并自动组装到测试用例集中，因此可以直接使用run()方法运行discover
discover = unittest.defaultTestLoader.discover(cases_dir, pattern='test_*.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d_%H-%M-%S_")
    filename = './report/' + now + 'result.html'
    fp = open(filename,'wb')

    runner = HTMLTestRunner(stream = fp, title="测试报告", description="用例执行情况", )
    runner.run(discover)
    fp.close()
