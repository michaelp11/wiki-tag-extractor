# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WikiTagExtractorItem(scrapy.Item):
    title = scrapy.Field()
    paragraph = scrapy.Field()
    tags = scrapy.Field()