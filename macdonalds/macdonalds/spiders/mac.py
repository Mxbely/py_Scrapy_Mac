import scrapy


class MacSpider(scrapy.Spider):
    name = "mac"
    allowed_domains = ["www.mcdonalds.com"]
    start_urls = ["https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html"]

    def parse(self, response):
        pass
