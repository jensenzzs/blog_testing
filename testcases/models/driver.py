from selenium.webdriver import Remote
from selenium import webdriver

#启动浏览器驱动
def browser():
    # driver = webdriver.Chrome()
    host = "http://192.168.52.43"
    # host = 'localhost' # 运行主机（默认：127.0.0.1）
    port = '5556' # 端口号（默认：4444）
    dc = {'browserName':'chrome'} # 指定浏览器('chrome','firefox')
    url = host + ':' + port + '/wd/hub'
    # print(url)
    driver = Remote(command_executor = url, desired_capabilities = dc)
    # driver = Remote(command_executor='http://192.168.52.43:5556/wd/hub', desired_capabilities=dc)    
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get("http://www.baidu.com")
    dr.quit()