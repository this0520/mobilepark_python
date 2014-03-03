# -*- coding: UTF-8 -*-

'''
Created on 2014. 2. 14.

@author: root
'''

import MySQLdb

db = MySQLdb.connect(host='localhost',user='root', passwd='root123', db='python')
db.autocommit(True)

cursor = db.cursor()
cursor.execute("select * from test")
rows = cursor.fetchall()

for row in rows:
    for column in row:
        print(column),
    
#row = result.fetchone()


cursor.close()
db.close()