goto :main

"start"  命令可以打开两个窗口同时运行程序
"rem"    单行注释
"goto :**" 与 ":**" 之间的内容不会被运行，可以当做多行注释

:main

rem 本机启动selenium server hub
start java -jar ./driver/selenium-server-standalone-3.4.0.jar -role hub

rem 本机启动selenium server node
start java -jar ./driver/selenium-server-standalone-3.4.0.jar -role node -port 5555
