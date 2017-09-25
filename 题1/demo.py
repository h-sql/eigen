# coding=utf-8
__author__ = 'sql'

with open('FileInput.txt', 'r') as f:
	for line in f:
		with open('WrongWord-stock.txt', 'r') as f1:
			for line1 in f1:
				if line1 in line:
					print '错字: ', line1
				else:
					print '语句完美 '

