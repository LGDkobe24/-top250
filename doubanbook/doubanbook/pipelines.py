#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
------------------------------------------------------------
# @Date    : 2015-03-11 15:38:28
# @Author  : 潘嘉朋 (385334338@qq.com)
# @Version : 0.0.1
# @功能     :连接mongodb、mysql的pipeline

------------------------------------------------------------
"""
import pymongo
import MySQLdb
import MySQLdb.cursors


from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class MongodbPipeline(object):
	def __init__(self):
		self.server = settings['MONGODB_SERVER']
		self.port = settings['MONGODB_PORT']
		self.db = settings['MONGODB_DB']
		self.collection = settings['MONGODB_COLLECTION']
		connection = pymongo.Connection(self.server, self.port)
		db = connection[self.db]
		self.collection =db[self.collection]

	def process_item(self, item, spider):

		err_msg = ''
		for field, data in item.items():
			if not data:
				err_msg += "Missing %s of data from %s\n" % (field, data)
		if err_msg:
			raise DropItem(err_msg)
		self.collection.insert(dict(item))
		log.msg("Item Wrote to Mongodb database %s%s" %
				(self.db, self.collection),
				level = log.DEBUG, spider= spider)
		return item

class MysqlPipeline(object):
	def __init__(self):
		self.dbpool = adbapi.ConnectionPool('MySQLdb',
				host = 'localhost',
				db = 'python',
				user ='root',
				passwd = 'pjp19911023',
				cursorclass = MySQLdb.cursors.DictCursor,
				charset = 'utf8',
				use_unicode = False
			)
	def process_item(self, item, spider):
		query = self.dbpool.runInteraction(self._conditional_insert, item)
		query.addErrback(self.handle_error)
		return item

	def _conditional_insert(self, tx, item):
		tx.execute("select * from book where b_name= %s",(item['name']))
		result=tx.fetchone()
		log.msg(result,level=log.DEBUG)
		print result
		if result:
			log.msg("Item already stored in db:%s" % item,level=log.DEBUG)
		else:
			tx.execute("insert into book (b_name,b_Press,b_author,b_comment) values (%s,%s,%s,%s)",
				(item['name'],item['Press'],item['author'],item['comment']))
			log.msg("Item stored in db: %s" % item, level=log.DEBUG)
    
    	def handle_error(self, e):
    		log.err(e)

