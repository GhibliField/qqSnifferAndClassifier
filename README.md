1 Requirement
-----------
在一些业务场景中需要拿到IM上的通信记录来做一些数据分析，例如对QQ平台中的消息进行领域分类等。
 
2 Environment & Tools
-----------

- python 2.7
- Ubuntu 16.04
- ElasticSearch 5.5.2
- Kibana 5.5.2
- Firefox 57.0.1 (64-bit)

**Python third party dependencies：**

- pypcap(1.2.0)【捕包】
- dpkt(1.9.1)【解析包】
- elasticsearch(6.0.0) 【es的python客户端】
- tgrocery(0.1.3)【短文本分类】

3 Run
-----------

	python2 getqqinfo.py

