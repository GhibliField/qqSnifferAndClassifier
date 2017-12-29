# -*- coding=utf-8 -*-

from elasticsearch import Elasticsearch
import hashlib
class Index2ES:
	def __init__(self,index,doctype,response_body):
		self.body=response_body
		self.index=index
		self.doctype=doctype
		self.id=hashlib.md5(str(response_body['time'])).hexdigest()
		self.es = Elasticsearch()

	def putdoc(self):
		print(self.es.index(index=self.index,doc_type=self.doctype,id=self.id,body=self.body))




	

