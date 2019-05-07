#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql

def get_Ip(num):
    conn = pymysql.connect(host='rm-bp1w1p1b35c3g17caeo.mysql.rds.aliyuncs.com', user='evan_wang',password='Evan#8718196', db ='spider',port=3306, charset='utf8')
    print('连接数据库成功！')
    cursor = conn.cursor()

    sql = '''select IPtest_address from IPaddress'''

    proxies_list =[]
    try:
        cursor.execute(sql)
        conn.commit()
        result1 = list(cursor.fetchmany(num))
        for i in range(len(result1)):                             #将元组转变为列表
            mk = list(result1[i])
            proxies_list = mk + proxies_list
    except:
         cursor.rollback()
         print('读取失败')
    cursor.close()
    conn.close()
    return proxies_list
