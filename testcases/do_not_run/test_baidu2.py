import package.HTMLTestRunner
import unittest
from selenium import webdriver
from package.HTMLTestRunner import HTMLTestRunner

class Baidu(unittest.TestCase):
    '''百度测试'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com/"

    def test_baidu_search(self):
        '''百度搜索测试'''

        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()

    def test_baidu_search2(self):
        '''百度搜索测试2'''

        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":

    '''
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))

    # 定义报告存放的位置
    fp = open('./package/result.html','wb')

    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况：')

    runner.run(testunit) # 运行测试用例
    fp.close() # 关闭报告文件
    '''