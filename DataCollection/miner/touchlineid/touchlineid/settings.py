# -*- coding: utf-8 -*-

# Scrapy settings for touchlineid project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'touchlineid'

SPIDER_MODULES = ['touchlineid.spiders']
NEWSPIDER_MODULE = 'touchlineid.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'touchlineid (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'touchlineid.pipelines.SaveEntriesPipeline': 1
    }
