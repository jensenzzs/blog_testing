# -*- coding:utf8 -*-
import mysql.connector

class MSSQL:
    def __init__(self, host, port, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.port = port
    def __GetConnect(self):
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = mysql.connector.connect(host=self.host, port = self.port, user=self.user, password=self.pwd, database=self.db, charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur
    def ExecQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.conn.close()
        return resList
    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

def main():
    db = MSSQL(host="localhost", port=3306, user=r"sa", pwd=r"mm136438", db=r"test")
    for i in range(300):
        reslist = db.ExecQuery("select * from test where order_num='SP000112181494405414218'")
        num = len(reslist)
        if num != 0:
            print(num)
            break
        print('第%r次查询...' % (i + 1))

        # print(i, j.encode('latin-1').decode('gbk'))


if __name__ == '__main__':
    main()
