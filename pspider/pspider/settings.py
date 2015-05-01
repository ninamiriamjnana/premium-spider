# -*- coding: utf-8 -*-

# Scrapy settings for pspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'pspider'

SPIDER_MODULES = ['pspider.spiders']
NEWSPIDER_MODULE = 'pspider.spiders'

ITEM_PIPELINES = {
    'pspider.pipelines.PeeweePipeline': 300
    }

DOWNLOAD_DELAY = 0.25    # 250 ms of delay

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pspider (+http://www.yourdomain.com)'
