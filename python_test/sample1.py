# -*- coding: UTF-8 -*-

'''
Created on 2014. 2. 17.

@author: root
'''

import sys
import datetime
import os
import commands
import subprocess
import MySQLdb

today = datetime.datetime.today()
year = today.year
month = today.month
day = today.day

check_date = ""

uptime = ""
load_avg = ""

task_temp = ""
cpu_temp = ""
mem_temp = ""
swap_temp = ""

fileName = today.strftime('%Y-%m-%d') + '.log'

def top(data):
    print("[ top ] : " + data)
    check_date = data[1:18].replace(" ","").replace("-","").replace(":","")
    temp = data[27:].split(",", 3)
    uptime = temp[0].strip() + temp[1].rstrip()
    load_avg = temp[3][15:]
    return check_date, uptime, load_avg
    
def task(data):
    print("[ Tasks ] : " + data)
    temp = data[27:].split(",")
    return temp
    
def cpu(data):
    print("[ cpu ] : " + data)
    temp = data[28:].split(",")
    return temp

def mem(data):
    print("[ mem ] : " + data)
    temp = data[26:].split(",")
    return temp

def swap(data):
    print("[ swap ] : " + data)
    temp = data[27:].split(",")
    return temp

#row_data(fileName)
#f = open("/root/workspace/python/python_test/row_data.txt","r")

p = os.popen('tail -6 /root/workspace/python/python_test/'+fileName, 'r')

cnt = 0



while 1:
    cnt += 1
    line = p.readline()
    if not line : break
    if cnt == 1:
        ckeck_date, uptime, load_avg = top(line)
    elif cnt == 2:
        task_temp = task(line)
    elif cnt == 3:
        cpu_temp = cpu(line)
    elif cnt == 4:
        mem_temp = mem(line)
    elif cnt == 5:
        swap_temp = swap(line)
    else:
        break
    
print("="*70)
print("ckeck_date => " + ckeck_date)
print("uptime => " + uptime)
print("load_avg => " + load_avg)

print("task_total => " + task_temp[0].strip().split(" ")[0])
print("task_run => " + task_temp[1].strip().split(" ")[0])
print("task_sleep => " + task_temp[2].strip().split(" ")[0])
print("task_stop => " + task_temp[3].strip().split(" ")[0])
print("task_zombie => " + task_temp[4].strip().split(" ")[0])

print("cpu_user => " + cpu_temp[0].strip()[:-3])
print("cpu_system => " + cpu_temp[1].strip()[:-3])
print("cpu_net => " + cpu_temp[2].strip()[:-3])
print("cpu_idle => " + cpu_temp[3].strip()[:-3])

print("mem_total => " + mem_temp[0].strip().split(" ")[0])
print("mem_used => " + mem_temp[1].strip().split(" ")[0])
print("mem_free => " + mem_temp[2].strip().split(" ")[0])
print("mem_buffer => " + mem_temp[3].strip().split(" ")[0])

print("swap_total => " + swap_temp[0].strip().split(" ")[0])
print("swap_used => " + swap_temp[1].strip().split(" ")[0])
print("swap_free => " + swap_temp[2].strip().split(" ")[0])
print("swap_cache => " + swap_temp[3].strip().split(" ")[0])

print("="*70)

task_total =task_temp[0].strip().split(" ")[0]
task_run = task_temp[1].strip().split(" ")[0]
task_sleep = task_temp[2].strip().split(" ")[0]
task_stop = task_temp[3].strip().split(" ")[0]
task_zombie = task_temp[4].strip().split(" ")[0]

cpu_user = cpu_temp[0].strip()[:-3]
cpu_system = cpu_temp[1].strip()[:-3]
cpu_net = cpu_temp[2].strip()[:-3]
cpu_idle = cpu_temp[3].strip()[:-3]

mem_total = mem_temp[0].strip().split(" ")[0]
mem_used = mem_temp[1].strip().split(" ")[0]
mem_free = mem_temp[2].strip().split(" ")[0]
mem_buffer = mem_temp[3].strip().split(" ")[0]

swap_total = swap_temp[0].strip().split(" ")[0]
swap_used = swap_temp[1].strip().split(" ")[0]
swap_free = swap_temp[2].strip().split(" ")[0]
swap_cache = swap_temp[3].strip().split(" ")[0]

db = MySQLdb.connect(host='localhost',user='root', passwd='root123', db='python')
db.autocommit(True)

param = [(ckeck_date, uptime, load_avg, task_total, task_run, task_sleep, task_stop, task_zombie, cpu_user, cpu_system, cpu_net, cpu_idle, mem_total, mem_used, mem_free, mem_buffer, swap_total, swap_used, swap_free, swap_cache)]
cursor = db.cursor()
cursor.executemany('insert into tbl_top_log values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', param)

cursor.close()
db.close()