#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by Susie Rao Xi, 2016-01-13
# get the coordinates (latitude and longitude from google geocode)
# call the program in terminal python get_miss_coor.py file_miss.csv

import sys, codecs, re, urllib, urllib2, json
from collections import defaultdict
file_miss=sys.argv[1]

infile_miss=codecs.open(file_miss,'r', "utf-8")
miss_dict={}
outfile=codecs.open("coor.txt", 'w', 'utf-8')
outfile.write("zip"+'\t'+'lat'+'\t'+'lng'+'\t'+'freq'+'\n')
def decode_address_to_coordinates(address):
        params = {
                'address' : address,
                'sensor' : 'false',
        }  
        url = 'http://maps.google.com/maps/api/geocode/json?' + urllib.urlencode(params)
        response = urllib2.urlopen(url)
        result = json.load(response)
        try:
                return result['results'][0]['geometry']['location']
        except:
                return None
# Sample format: {u'lat': 23.0021096, u'lng': 114.0723599}

 
for line_miss in infile_miss:
	m_miss=re.search(r'(\d+)\t(\d+)\n', line_miss)
	if m_miss:
		zip_miss=m_miss.group(1)
		freq=m_miss.group(2)
		out=decode_address_to_coordinates("China, Guangdong"+zip_miss)
		#print(out_coor, zip_miss, freq)
		#({u'lat': 23.1550437, u'lng': 113.2228394}, u'510165', u'56')
		if out is not None: 
		#miss_dict[zip_miss]=(out.values()[0], out.values()[1], freq)
			outfile.write('%s\t%s\t%s\t%s\n'%(zip_miss, out.values()[0], out.values()[1], freq))
#print(miss_dict)
		if out is None:
			outfile.write('%s\t%s\t%s\t%s\n'%(zip_miss, 'NA', 'NA', freq))

infile_miss.close()
outfile.close()
