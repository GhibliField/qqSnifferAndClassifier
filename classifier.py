#! /usr/bin/env python2
# -*-coding:utf-8 -*-

from tgrocery import Grocery
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Classifier:
	def __init__(self,shorttext):
		self.shorttext=shorttext
		
	def labelmaker(self):
		result=[]
		grocery = Grocery('11c_20k_20171226')
		grocery.load()	
		label_confidence=sorted(grocery.predict(self.shorttext).dec_values.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)[0]
		result.append(label_confidence[0])#置信度最高的分类结果
		result.append(label_confidence[1])# 置信度
		return result

if __name__=='__main__':
	print Classifier('他还有好多鲜为人知的秘密呢').labelmaker()