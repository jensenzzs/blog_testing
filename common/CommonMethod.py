# -*- coding: utf-8 -*-
# http://172.19.130.142:5984/code/_design/testpos/600/index.html
# http://172.19.130.142:5984/code/_design/pos/600/index.html
# C:\Users\Jin-K\AppData\Local\Google\Chrome\User Data

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from pyexcel_xls import get_data
import datetime
import time
import re

# 打开网页
# self.driver = webdriver.PhantomJS()
# chrome_options.add_argument("--start-maximized")#最大化
# chrome_options.add_argument("--kiosk")#全屏
# chrome_options.add_argument("--disable-web-security")#跨域

def open_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--kiosk")
    chrome_options.add_argument("--disable-web-security")#跨域
    chrome_options.add_argument("--user-data-dir=C:/Test Data")
    driver = webdriver.Chrome(executable_path="./../../lib/chromedriver.exe", chrome_options=chrome_options)
    # driver.set_window_size(1024, 910)
    return driver


# 等待并找到元素,返回值为该元素
# loc为元素信息,例如loc = (By.ID,'001')
def find_ele(driver, loc, t=3):
    try:
        return driver.find_element(*loc)
    except:
        try:
            return WebDriverWait(driver, t, 0.5).until(EC.presence_of_element_located(loc))
        except:
            print(u"找不到元素: " + str(loc))
            # assert False, u"找不到元素: " + str(loc)


# 等待并找到元素集,返回值为该元素集
def find_eles(driver, loc, t=3):
    try:
        return driver.find_elements(*loc)
    except:
        try:
            return WebDriverWait(driver, t, 0.5).until(EC.presence_of_all_elements_located(loc))
        except:
            print(u"找不到元素: " + str(loc))
            # assert False, u"找不到元素: " + str(loc)


# 判断某个元素是否被加到了dom树里, 并不代表该元素一定可见, 返回true/false
def check_ele_existed(driver, loc, t=3):
    try:
        WebDriverWait(driver, t, 0.5).until(EC.presence_of_element_located(loc))
        return True
    except:
        return False


# 判断某个元素是否可见并且是enable的，代表可点击, 返回true/false
def check_ele_can_click(driver, loc, t=3):
    try:
        WebDriverWait(driver, t, 0.5).until(EC.element_to_be_clickable(loc))
        return True
    except:
        return False


# 判断指定的元素中是否包含了预期的字符串,返回布尔值;可用来检查提示框等
# 't'为默认等待时间
# 'log'为print_log,1 = 有,0 = 没有
def check_str_in_ele_text(driver, ms, loc=(By.ID, 'myAlert'), t=3, log=0):
    assert check_ele_can_click(driver, loc, t=t), "元素" + str(loc) + "不显示/不可点击"
    try:
        WebDriverWait(driver, t, 0.5).until(EC.text_to_be_present_in_element(loc, ms), str(loc))
        if log == 1:
            print(u"实际结果:" + str(find_ele(driver, loc).text))
        return True
    except:
        return False


# 获取xlsx文件
def get_xlsx_file(file_name):  # 返回一个字典
    xls_file = './../../data/' + str(file_name) + '.xlsx'
    try:
        return get_data(xls_file)
    except:
        print('不存在文件:%r'%(xls_file))



# 常规输入框
def input_value_to_input(driver, loc, value):
    # WebDriverWait(driver,10).until(EC.element_to_be_clickable(loc),"元素" + str(remind_mes) + "不可点击")
    find_ele(driver, loc).clear()
    find_ele(driver, loc).send_keys(value)


# ul_id = 下拉选择单的ID
# 函数实现判断下拉选择单是否存在
def check_select_ul_is_null(driver, ul_id):
    ul_value_xpath = ".//*[@id = '" + ul_id + "']/li"
    return check_ele_can_click(driver, ul_value_xpath)


# select_list_xp_loc = 下拉选择单的xp，check_list = 要检查的值组成的列表(注意:第一项为空也要输入)
# 函数实现检查下拉单显示的信息是否和check_list一致
def check_select_list_value(driver, ul_id, check_list):
    assert check_select_ul_is_null(driver, ul_id), '选择单为空!'
    list_value_xpath = ".//*[@id = '" + ul_id + "']/li"
    list_va = driver.find_elements_by_xpath(list_value_xpath)
    l1 = len(check_list)
    i = 0; m = 0
    while i < l1:
        for list_value in list_va:
            if list_value.text == check_list[i]:
                m += 1
        if m == 1:
            print(check_list[i] + u"is_ok_!")
        else:
            print(check_list[i] + u"is_Error_!")
            return False
        m = 0
        i += 1
    print("check_over_!")
    return True


# 选择单中选择某项
def choose_value_from_select(driver, click_ele, ul_xp, choose_val):
    assert check_ele_can_click(driver, ul_xp), '选择单为空!'
    print("I want to choose:" + str(choose_val))
    find_ele(driver, click_ele,).click()
    find_ele(driver, (By.ID, ul_xp))
    display_list = find_eles(driver, (By.XPATH, "//ul[@id = '" + str(ul_xp) + "']/li"))
    i = 1
    for ele in display_list:
        if choose_val == ele.text:
            target_xpath = "//ul[@id = '" + str(ul_xp) + "']/li[" + str(i) + "]"
            print(str(choose_val) + "的xpath: " + str(target_xpath))
            target_ele = (By.XPATH, target_xpath)
            find_ele(driver, target_ele).click()
            break
        i = i + 1
    raise ("找不到目标选项: " + choose_val)


# 函数实现值的有序的表单输入(值和选项)和按钮点击
# 有序输入:list_data = [["xpath路径","值"],["xpath路径","值"]"];例如:list_data = [[(By.ID,"1"),(By.ID,"2")],[(By.ID,"3"),4]]
# 有序点击:list_data = ["xpath路径","xpath路径"]
def input_data(driver, list_data):
    if type(list_data[0]) is list:
        for i in list_data:
            if type(i[1]) is tuple:
                find_ele(driver, i[0]).click()
                find_ele(driver, i[1]).click()
                print('success_select_from_list_!')
            # elif type(i[1]) is not tuple:
            else:
                input_value_to_input(driver, i[0], i[1])
                print('success_input_from_list_!')
                # else:
                #     raise ('Please check the content of the print!')
    else:
        for i in list_data:
            find_ele(driver, i).click()
        print('success_click_from_list_!')


# tab_id = 表格ID名字
# 函数实现判断表格是否存在
def check_table_is_null(driver, tab_id):
    table_xpath = ".//*[@id = '" + tab_id + "']"
    table_value_xpath = table_xpath + '//tr[1]/td[1]'
    return check_ele_can_click(driver, table_value_xpath)


# tab_id = 表格ID名字
# 把所要检查的列数和检查值制作一个字典,例如：case_dict = {"row1":"val1","row2":"val2"}
# 函数实现检查表格当前页中的值是否和检查值一致
def check_table_current_page(driver, tab_id, case_dict):
    assert check_table_is_null(driver, tab_id), '该表格为空!'
    table_xpath = ".//*[@id = '" + tab_id + "']"

    dic = case_dict
    for row, val in dic.items():
        i = 0
        td = table_xpath + '//tr/td[' + row + ']'
        lis = driver.find_elements_by_xpath(td)
        for e in lis:
            i += 1
            if not re.search(val, e.text):
                print(i, '_row_', e.text, " didn't match ", val)
                return False
                # else:
                #     print(i,'__',e.text,'_is_',str(val),'_____ok')
    print('check_pass_!')
    return True


# 该函数需要根据实际情况进行修改
# driver,tab_id = 表格ID名字,first_page_icon_loc = 首页,next_page_icon_loc = 下一页
# 把所要检查的列数和检查值制作一个字典,例如：case_dict = {"row1":"val1","row2":"val2"}
# 函数实现检查表格所有页中的值是否和检查值一致
def check_table_all_page(driver, tab_id, case_dict, first_page_icon_loc, next_page_icon_loc):
    assert check_table_is_null(driver, tab_id), '该表格为空!'
    table_xpath = ".//*[@id = '" + tab_id + "']"

    first_page_icon_xp = first_page_icon_loc[1]
    # print(first_page_icon_xp)
    next_page_icon_xp = next_page_icon_loc[1]

    up_first_xp = first_page_icon_xp.replace("/span", "")
    up_next_xp = next_page_icon_xp.replace("/span", "")

    up_first_class = driver.find_element_by_xpath(up_first_xp).get_attribute("class")
    up_next_class = driver.find_element_by_xpath(up_next_xp).get_attribute("class")

    dic = case_dict
    new_next_class = up_next_class
    while new_next_class == up_next_class:
        new_next_class = driver.find_element_by_xpath(up_next_xp).get_attribute("class")
        for row, val in dic.items():
            td = table_xpath + '//tr/td[' + str(row) + ']'
            lis = driver.find_elements_by_xpath(td)
            i = 0
            for e in lis:
                i += 1
                if not re.search(val, e.text):
                    print(i, '_row_', e.text, " didn't match ", val)
                    return False
                    # else:
                    #     print(e.text,' match ',val)
        driver.find_element_by_xpath(next_page_icon_xp).click()
        time.sleep(1.5)
        new_first_class = driver.find_element_by_xpath(up_first_xp).get_attribute("class")
        if up_first_class == new_first_class:
            break
    driver.find_element_by_xpath(first_page_icon_xp).click()
    return True


# driver,tg_row = 所要检查的列,tg_val = 检查的值,tab_id = 表格ID名字,first_page_icon_loc = 首页,next_page_icon_loc = 下一页
# 函数实现检查某列日期是否在b_date 以及 e_date之间
# 比如我的b_date 为“2014-01-03”，我的e_date为“2014-01-05”，那么该列的日期如果在“2014-01-03”到“2014-01-05”之间都判定为匹配
# b_date 以及 e_date采用 "2016-01-03" 格式
def check_table_date_all_page(driver, tab_id, target_row, b_date, e_date, first_page_icon_loc, next_page_icon_loc):
    assert check_table_is_null(driver, tab_id), "该表格为空!"
    table_xpath = ".//*[@id = '" + tab_id + "']"

    begin_date = datetime.datetime.strptime(b_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(e_date, '%Y-%m-%d')

    first_page_icon_xp = first_page_icon_loc[1]
    next_page_icon_xp = next_page_icon_loc[1]

    up_first_xp = first_page_icon_xp.replace("/span", "")
    up_next_xp = next_page_icon_xp.replace("/span", "")

    up_first_class = driver.find_element_by_xpath(up_first_xp).get_attribute("class")
    up_next_class = driver.find_element_by_xpath(up_next_xp).get_attribute("class")

    new_next_class = up_next_class
    while new_next_class == up_next_class:
        new_next_class = driver.find_element_by_xpath(up_next_xp).get_attribute("class")
        td = table_xpath + '//tr/td[' + str(target_row) + ']'
        lis = driver.find_elements_by_xpath(td)
        i = 0
        for e in lis:
            i += 1
            current_date = datetime.datetime.strptime(e.text, '%Y-%m-%d')
            if not current_date <= end_date and current_date >= begin_date:
                print(i, '_row_', e.text, " 不在时间范围之内 ")
                # else:
                #     print(i,'_row_',e.text," _is_OK ")
        driver.find_element_by_xpath(next_page_icon_xp).click()
        time.sleep(1.5)
        new_first_class = driver.find_element_by_xpath(up_first_xp).get_attribute("class")
        if up_first_class == new_first_class:
            break
    driver.find_element_by_xpath(first_page_icon_xp).click()
    return True
