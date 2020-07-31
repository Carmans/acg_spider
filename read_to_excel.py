# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 19:22
# @Author  : Zhang Fei
# @Site    :
# @File    : b2b_baidu.py
# @Software: PyCharm
# 爱采购主表商品主页数据采集

# import xlwt
# import os
#
#
# pic_path='C:\Users\zhangfei\Desktop\商品'

import os
import os.path

rootdir = "./商品"
file_object = open('train_list.txt','w')
for parent,dirnames,filenames in os.walk(rootdir):
 for filename in filenames:
  print(filename)
  file_object.write(filename+ '\n')
file_object.close()



# fo = open("file_list.txt", "w")  # 打开文件
#
#
#
# # 创建workbook（其实就是excel，后来保存一下就行）
# workbook = xlwt.Workbook(encoding='utf-8')
# # 创建表
# worksheet = workbook.add_sheet('提取完的图片sku编码')
#
#
#
# worksheet.write(1, 1, label="商品描述")
#
# # 保存文件为excel
# workbook.save('图片SKU编码提取.xls')



