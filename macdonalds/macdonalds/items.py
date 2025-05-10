# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MacdonaldsItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    calories = scrapy.Field()
    fats = scrapy.Field()
    carbs = scrapy.Field()
    proteins = scrapy.Field()
    unsaturated_fats = scrapy.Field()
    sugar = scrapy.Field()
    salt = scrapy.Field()
    portion = scrapy.Field()
