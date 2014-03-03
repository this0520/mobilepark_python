# -*- coding: UTF-8 -*-

'''
Created on 2014. 2. 5.

@author: this0520
'''

import sys
import datetime
import os
import commands
import subprocess

def linePrint(time):
    return '[' + time + ']' + ('='*50) + '\n'
    
today = datetime.datetime.today()
year = today.year
month = today.month
day = today.day

fileName = today.strftime('%Y-%m-%d') + '.log'
time = today.strftime('%Y-%m-%d %H:%M:%S')

f = open('/root/workspace/python/python_test/'+fileName, 'a')

f.write(linePrint(time))

txt = os.system('/root/workspace/python/python_test/top.sh')
top = open('/root/workspace/python/python_test/top.log','r')
for x in range(5):
    topLog = top.readline()
    f.write('[' + time + ']' + topLog)
    
#top.close()


#top = subprocess.Popen("top -p 1 -n 1", "r")
#text = top.read()
#print(text)

f.write(linePrint(time))

f.close()
