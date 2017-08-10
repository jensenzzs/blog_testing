from selenium import webdriver
import os

#截图函数

def printscreen(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('/testcases')[0]
    file_path = base + "/report/screenshots/" + file_name
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://zhouzhengsheng.com")
    printscreen(driver,'zhouzhengsheng.jpg')
    driver.quit()
