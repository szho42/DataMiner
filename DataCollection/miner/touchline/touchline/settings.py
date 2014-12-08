# -*- coding: utf-8 -*-

# Scrapy settings for touchline project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'touchline'

SPIDER_MODULES = ['touchline.spiders']
NEWSPIDER_MODULE = 'touchline.spiders'

ITEM_PIPELINES = {
    'touchline.pipelines.CSVWriterPipeline2': 1
    }
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'touchline (+http://www.yourdomain.com)'
