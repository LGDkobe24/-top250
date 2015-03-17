# -*- coding: utf-8 -*-

# Scrapy settings for doubanbook project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'doubanbook'

SPIDER_MODULES = ['doubanbook.spiders']
NEWSPIDER_MODULE = 'doubanbook.spiders'

ITEM_PIPELINES = {'doubanbook.pipelines.MysqlPipeline': 1}

LOG_LEVEL = 'DEBUG'

DOWNLOAD_DELAY = 2
RANDMIZE_DOWNLOAD_DELAY = True

USER_AGENT = 'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'
COOKIES_ENABLED = True

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'python'
MONGODB_COLLECTION = 'pjp'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'doubanbook (+http://www.yourdomain.com)'
