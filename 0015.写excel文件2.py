#!/usr/bin/env python
#coding: utf-8
import os
import json
import xlwt

# 存放文件的目录
filepath = '/home/bill/Desktop'

def run():
    os.chdir(filepath)
    # 读取文件内容
    with open('city.txt') as f:
        content = f.read()
    # 转为json
    d = json.loads(content)
    file = xlwt.Workbook()
    # 添加sheet
    table = file.add_sheet('test')
    for row, i in enumerate(list(d)):
        table.write(row, 0, i)
        table.write(row, 1, d[i])
    file.save('city.xls')

if __name__ =="__main__":
    run()
