'''
Created on 2016年4月19日

mysql 数据库连接

使用pymysql连接

@author: liyut

@version: python3.5

'''
import pymysql;

url = 'localhost';
user = 'root';
password = 'root';
port = '3306';
   
def openMysql(url,user,password,port):
 
    try:
        print('开始连接数据库'+port);
        conn = pymysql.connect(
                               host='localhost',
                               port='3306',
                               user='root',
                               passwd='root',
                               db='demo',
                               charset='UTF-8'
                               );  
        cur = conn.cursor();
        cur.execute(" SELECT * FROM t_user ");   
        print('获取数据：'+cur)                 
        conn.close();   
                                          
    except Exception:
        print('数据库连接异常');


cn = openMysql(url,user,password,port);