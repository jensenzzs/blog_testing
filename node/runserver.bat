java -jar .\selenium-server-standalone-3.4.0.jar -role node -port 5555 -hub http://192.168.1.102:4444
-Dwebdriver.ie.driver=".\IEDriverServer.exe" 
-Dwebdriver.chrome.driver=".\chromedriver.exe"
-Dwebdriver.chrome.driver=".\geckodriver.exe"
# -Dwebdriver.firefox.bin="F:\Program Files (x86)\Mozilla Firefox\firefox.exe" 
# -browser "browserName=internet explorer,maxInstances=5,version=11,platform=WINDOWS" 
# -browser "browserName=chrome,maxInstances=2,version=47,platform=WINDOWS" 
# -browser "browserName=firefox,maxInstances=3,version=38,platform=WINDOWS"