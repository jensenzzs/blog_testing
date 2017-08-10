## 测试项目说明

## 目录结构说明
 - `common`: 用来存放通用的方法、函数等。
 - `data`: 用来存放测试所需数据，例如：参数化数据。
 - `driver`: 用来存放selenium-server-standalone-3.4.0.jar、各个浏览器的webdriver等，在测试之前需要根据执行场景将浏览器驱动复制到系统的环境变量path目录下。
 - `package`: 用来存放自动化所用到的扩展包。例如，HTMLTestRunner.py是一个单独的模块，并对其做了修改。在执行测试用例前，需要将其放置到Python的Lib目录下。
 - `report`: 用来存放测试报告、测试截图等。
 - `testcases`: 用来存放测试用例。
   - `do_not_run`: 用来存放不希望运行的测试用例。
   - `models`: 用来存放一些公共的配置函数及公共类。
   - `page_object`: 用于存放测试用例的页面对象，根据自定义规则，以`*Page.py`命名的文件为封装的页面对象文件。
   - `*.sta.py`: 测试用例文件，以`*.sta.py`命名的文件将被当作自动化测试用例执行。
 - `runtest.py`: 项目主程序，用来执行项目测试用例。
 - `startup.bat`: Windows批处理文件，用于测试用例运行前，测试环境的准备。例如：启动selenium server服务。

 ## 运行所需环境
 - Windows 10
 - Python 3
 - selenium 3

 ## 执行顺序说明
  1. 运行`startup.bat`，配置selenium server hub服务
  2. ​运行`runtest.py`，执行测试用例