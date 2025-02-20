import scrapy
import logging
from macdonalds.separators import get_item_id

logger = logging.getLogger(__name__)

MAIN_URL = "https://www.mcdonalds.com"
mac_api_detail_url = f"{MAIN_URL}/dnaapp/itemDetails?country=UA&language=uk&showLiveData=true&item="

class MacSpider(scrapy.Spider):
    name = "mac"
    allowed_domains = ["www.mcdonalds.com"]
    start_urls = [f"{MAIN_URL}/ua/uk-ua/eat/fullmenu.html"]

    def parse(self, response):
        main_menu = response.css("div.product-category")
        links = main_menu.css("a::attr(href)").extract()
        logger.info("Spider is working")

        for link in links:
            item_id = get_item_id(link)
            url = mac_api_detail_url + item_id
            yield response.follow(url, self.parse_dish_details)
    
    def parse_dish_details(self, response):
        dish_details = response.json()["item"]
        nutrients = dish_details["nutrient_facts"]["nutrient"]
        item_name = dish_details["item_name"]

        if "®" in item_name:
            item_name = item_name.replace("®", "")

        yield {
            "name": item_name,
            "description": dish_details["description"],
            "calories": nutrients[2]["value"],
            "fats": nutrients[3]["value"],
            "carbs": nutrients[5]["value"],
            "proteins": nutrients[7]["value"],
            "unsaturated_fats": nutrients[4]["value"],
            "sugar": nutrients[6]["value"],
            "salt": nutrients[8]["value"],
            "portion": nutrients[0]["value"],
        }
