'''
Created on 2016年4月19日

mysql 数据库连接

使用pymysql连接

@author: liyut

@version: python3.5

'''
import pymysql;


print('开始连接数据库');
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       db='demo',
                       charset='utf8' #中文的编码格式
                       );#cursorclass=pymysql.cursors.DictCursor 输出数据为字典格式
try:                      
    with conn.cursor() as cursor:    
        sql = 'SELECT * FROM t_user'
        cursor.execute(sql)
        #执行查询所有fetchall，    fetchone查询一条
        result = cursor.fetchall()
        #print(result)
        for row in result:
            uid = row[0]
            userName = row[1]
            realName = row[2]
            date = row[3]
            print("uid=%s,userName=%s,realName=%s,date=%s" % \
                  (uid,userName,realName,date))
except:
    print('数据库异常！')
finally:          
    conn.close(); 




