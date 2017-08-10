from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_object")
from models import myunit, function
from page_object.loginPage import login

# HTMLTestRunner可以读取""" """或''' '''标记的注释，在测试类和方法添加这样的注释，就可以显示在测试报告中了。
class loginTest(myunit.MyTest):
    '''登陆测试'''

    # 测试用户登陆
    def user_login_verify(self, username="", password=""):
        login(self.driver).user_login(username, password)
    
    def test_login1(self):
        '''用户名、密码为空'''
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.error_hint_1(), "请输入用户名")
        self.assertEqual(po.error_hint_2(), "请输入密码")
        function.printscreen(self.driver, "user_pawd_empty.jpg")
    
    def test_login2(self):
        '''用户名正确、密码为空'''
        self.user_login_verify(username="admin")
        po = login(self.driver)
        self.assertEqual(po.error_hint_1(), "请输入密码")
        function.printscreen(self.driver, "pawd_empty.jpg")

    def test_login3(self):
        '''用户名为空、密码正确'''
        self.user_login_verify(password="admin")
        po = login(self.driver)
        self.assertEqual(po.error_hint_1(), "请输入用户名")
        function.printscreen(self.driver, "user_empty.jpg")

    def test_login4(self):
        '''用户名与密码不匹配'''
        character = random.choice('abcdefghijklmnopqrstuvwxyz')
        username = "admin:" + character
        password = "admin"
        self.user_login_verify(username, password)
        po = login(self.driver)
        self.assertEqual(po.error_hint_1(), "用户名或密码无效")
        function.printscreen(self.driver, "user_pawd_error.jpg")


if __name__ == "__mian__":
    unittest.main()