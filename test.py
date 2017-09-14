# -*- coding:utf-8 -*-
import pymysql

#连接数据库
conn = pymysql.connect(host='192.168.8.208', port=3306, user = 'root', passwd='tuandai_bm2015', db='tuandai_bm')

#创建游标
cur = conn.cursor()

business_id = 'TDC1012017082402'

#查询lcj表中存在的数据(暂时不知道如何发送两个语句)
cur.execute("select t2.`*`,t1.* from tb_process_approve as t1 left join tb_process_approve_user as t2 on t1.approve_id=t2.approve_id where business_id='"+ business_id +"';");

#fetchall:获取lcj表中所有的数据
ret1 = cur.fetchone()

# 暂时不知道如何根据字段名获取
print(ret1[1])