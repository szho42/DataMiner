# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TouchlineItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    game_id = scrapy.Field()
    nation = scrapy.Field()
    league = scrapy.Field()
    season = scrapy.Field()
    year = scrapy.Field()
    date = scrapy.Field()
    home_team = scrapy.Field()
    away_team = scrapy.Field()
    home_scores = scrapy.Field()
    away_scores = scrapy.Field()
    half_time_score = scrapy.Field()
    final_score = scrapy.Field()
     
