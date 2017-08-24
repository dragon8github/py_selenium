import pymysql

#连接数据库
conn = pymysql.connect(host='192.168.8.208', port=3306,user = 'root', passwd='tuandai_bm2015', db='tuandai_bm')

#创建游标
cur = conn.cursor()

#查询lcj表中存在的数据
cur.execute("select * from tb_parameter where para_type='version' and para_name='H5'");

#fetchall:获取lcj表中所有的数据
ret1 = cur.fetchall()

print(ret1)