# coding=utf-8
__author__ = 'sql'
import random

# 获取文件行数，用于取随机数
def file_sample():
	'''
	调用格式：>>> from BigTextFileReader import file_sample
		      >>> file_sample()
		      -------------
		      'Sample result is saved as SampleOutput.txt '
	'''
	count = 0
	with open('FileInput.txt', 'r') as f:
		# 逐行写入，基本不占内存
		for line in f:
			count += 1

	# 采样1000
	sample_size = 1000
	sample = random.sample(range(count), sample_size)

	# 采样并写入文件
	fw = open('SampleOutput.txt', 'w')
	with open('FileInput.txt', 'r') as f:
		count = 0
		for line in f:
			if count in sample:
				print line
				fw.write(line)
			count += 1
	print 'Sample result is saved as SampleOutput.txt '

	return
