java -jar .\selenium-server-standalone-3.4.0.jar -role node -port 5556 -hub http://192.168.52.43:4444
-Dwebdriver.ie.driver="D:\node\IEDriverServer.exe" 
-Dwebdriver.chrome.driver="D:\node\chromedriver.exe"  
-Dwebdriver.firefox.bin="F:\Program Files (x86)\Mozilla Firefox\firefox.exe" 
# -browser "browserName=internet explorer,maxInstances=5,version=11,platform=WINDOWS" 
# -browser "browserName=chrome,maxInstances=2,version=47,platform=WINDOWS" 
# -browser "browserName=firefox,maxInstances=3,version=38,platform=WINDOWS"