#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by Susie Rao Xi, 2016-01-13

# function: 
# to find the matching between two csv files:
# file_miss: zip, freq
# file_gd: id (non-needed), zip (needed, same zip many ads), city (needed), ad (in tuple), capital(non-needed), province (non-needed)

# -> file_miss ->csv
# -> file_gd: -id, -province, +zip, city, ad, capital 
   # -> {zip:[(city, ad), (...)]}

# call the program in terminal python3 misszip.py file_miss.csv file_gd.csv 

import sys, codecs, re
from collections import defaultdict
file_miss=sys.argv[1]
file_gd=sys.argv[2]

infile_miss=codecs.open(file_miss,'r', "utf-8")
infile_gd=codecs.open(file_gd, 'r',"utf-8")

miss_dict={}

for line_miss in infile_miss:
	m_miss=re.search(r'(\d+)\t(\d+)\n', line_miss)
	if m_miss:
		zip_miss=m_miss.group(1)
		freq=m_miss.group(2)
		miss_dict[zip_miss]=freq
		
#print(miss_dict)
#{...'523575': '19', '523423': '23'}

gd_dict={}

#match unicode [\u4e00-\u9fff]+
#sample = u'I am from 美国。We should be friends. 朋友。'
#for n in re.findall(r'[\u4e00-\u9fff]+',sample):
#    print(n)


for line_gd in infile_gd:
	m_gd=re.search(
	r'([\u4e00-\u9fff]+)\t(\d+)\t([\u4e00-\u9fff]+)\t(?:\w)\n', line_gd)
	if m_gd:
		ad=m_gd.group(1)
		zip_gd=m_gd.group(2)
		city=m_gd.group(3)
		gd_dict.setdefault(zip_gd, []).append((city,ad))
#print(gd_dict)
#{...'525138': [('化州市', '宝圩镇')], '529259': [('台山市', '公益镇'), ('台山市', '麦巷村')],...}

#check if any match
for zip_miss in miss_dict.keys():
	if zip_miss in gd_dict.keys():
		print("ok")


#s={"a":3,"b":4}
#b={"a":[(3,4),(23,4)],"c":[(6,1),(56,90)]}
#for i in s.keys():
#	if i in b.keys():
#		print("ok")
