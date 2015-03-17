#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
------------------------------------------------------------
# @Date    : 2015-01-11 14:49:33
# @Author  : 潘嘉朋 (385334338@qq.com)
# @Version : 0.0.1
# @功能     :爬取豆瓣读书网top250的书籍信息

------------------------------------------------------------
"""
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector 
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from doubanbook.items import DoubanbookItem

class BookSpider(CrawlSpider):
	name = "book"
	allow_domains = ["book.douban.com"]
	start_urls = ["http://book.douban.com/top250"]

	rules =[
		Rule(SgmlLinkExtractor(allow=(r'http://book.douban.com/top250\?start=\d+.*'))),

		Rule(SgmlLinkExtractor(allow=(r'http://book.douban.com/subject/\d+')),callback="prase_item")
	]

	def prase_item(self, response):
		sel = Selector(response)
		item = DoubanbookItem()
		item['name'] = sel.xpath('//*[@id="wrapper"]/h1/span/text()').extract()
		item['Press'] = sel.xpath('//*[@id="info"]/text()[3]').extract()
		item['author'] =sel.xpath('//*[@id="info"]/span[1]/a/text()').extract()
		item['comment'] =sel.xpath('//*[@id="comment-list-wrapper"]/div[1]/ul/li[1]/p/text()').extract()
		return item
