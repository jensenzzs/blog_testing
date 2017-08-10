from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    # 用户登陆界面

    # 定义此页面的url
    url = '/admin/login.php'


    # 抠元素：登录表单
    login_username_loc = (By.ID, "name")
    login_password_loc = (By.ID, "password")
    login_button_loc = (By.XPATH, "/html/body/div/div/form/p[3]/button")


    # 输入登陆用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)
    
    # 输入登陆密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    # 点击登陆按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 定义统一登陆入口
    def user_login(self, username="username", password="password"):

        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    # 抠元素：登陆结果提示
    error_hint_loc_1 = (By.XPATH, "/html/body/div[1]/ul/li[1]")
    error_hint_loc_2 = (By.XPATH, "/html/body/div[1]/ul/li[2]")

    # 用户名错误提示
    def error_hint_1(self):
        return self.find_element(*self.error_hint_loc_1).text

    # 密码错误提示
    def error_hint_2(self):
        return self.find_element(*self.error_hint_loc_2).text