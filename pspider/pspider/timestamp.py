#!/usr/bin/env python
#coding: utf8 


def get_date (timestamp):
	month_dict={'Jan':1, 'Feb':2, 'Mär':3, 'Apr':4, 'Mai':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dez':12}

	string_base=timestamp.split(',')
	md=string_base[0]
	month=md[6:9]
	day=md[10:12]
	
	y=string_base[1]
	year=y[1:5]

	date=year
	date+=('-')
	date+=(month)
	date+=('-')	
	date+=(day)
	return date
