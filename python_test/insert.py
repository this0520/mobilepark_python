# -*- coding: UTF-8 -*-

'''
Created on 2014. 2. 14.

@author: root
'''

import MySQLdb

db = MySQLdb.connect(host='localhost',user='root', passwd='root123', db='python')
db.autocommit(True)

cursor = db.cursor()
cursor.execute("insert into test value (%s, %s, %d)" % ("'python'","'Son H S'",3))

cursor.close()
db.close()
