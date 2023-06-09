# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeedmapItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    star = scrapy.Field()
    rating = scrapy.Field()
    add = scrapy.Field()
    name = scrapy.Field()
    co = scrapy.Field()
    medical = scrapy.Field()
    order = scrapy.Field()
    phone = scrapy.Field()






