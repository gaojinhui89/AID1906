"""
read_db.py
数据库读操作示例  select
"""

import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='root',
                     database='stu',
                     charset='utf8')

# 创建游标 (操作数据库语句,获取查询结果)
cur = db.cursor()

# 数据库操作
sql = "select name,age from class_1 where sex='m';"
cur.execute(sql)

# 获取查询结果
# one_row = cur.fetchone()
# print(one_row)  # 元组
#
# many_row = cur.fetchmany(3)
# print(many_row)  # 元组套元组

all_row = cur.fetchall()
print(all_row)  # 元组套元组

# 关闭游标和数据库
cur.close()
db.close()
