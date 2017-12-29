#! /usr/bin/env python2
# -*- coding:utf-8 -*-


#使用这个脚本从smart qq实时获取聊天消息，打印每一条消息的发送方ID(内部ID),接收方QQ号，消息内容和发送时间。

import pcap
import dpkt
import time
from indexmessage import Index2ES
from classifier import Classifier

def timestamp_datetime(value):
	format = '%Y/%m/%d %H:%M:%S'
	value = time.localtime(value)
	dt = time.strftime(format, value)
	return dt

def captData():
	pc=pcap.pcap('wlp5s0')  #参数可为网卡名，可以使用ifconfig命令查看
	pc.setfilter('tcp port 80')    #设置监听过滤器
	for ptime,pdata in pc:    #ptime为收到时间，pdata为收到数据
		pkt = dpkt.ethernet.Ethernet(pdata)  
		if pkt.data.data.__class__.__name__ != 'TCP':
			continue
		ip_data=pkt.data
		tcp_data=ip_data.data
		app_data=tcp_data.data#向上层层解析直到应用层的内容
	
		if app_data.find('poll_type')!=-1:#以特定字符串作为有消息的标识
			process(app_data)


def process(app_data):
	#content=json.loads(app_data.split('\n\n')[-1])
	contentdict=eval(app_data.split('keep-alive')[-1].strip())
	
	message={}
	message['label']={}
	message['label']['tag']=Classifier(contentdict['result'][0]['value']['content'][1]).labelmaker()[0]
	message['label']['confidence']=Classifier(contentdict['result'][0]['value']['content'][1]).labelmaker()[1]
	message['from_id']=contentdict['result'][0]['value']['from_uin']
	message['to_id']=contentdict['result'][0]['value']['to_uin']
	message['time']=timestamp_datetime(contentdict['result'][0]['value']['time'])
	message['content']=contentdict['result'][0]['value']['content'][1]
	print 'MESSAGE: ',message['content']
	print 'FROM: ',message['from_id']
	print 'TO: ',message['to_id']
	print 'TIME: ',message['time']
	print 'LABEL: ',message['label']['tag']
	print 'CONFIDENCE: ',message['label']['confidence']

	index(message)
def index(doc):
	Index2ES('qq','messages',doc).putdoc()

if __name__=='__main__':
	captData()