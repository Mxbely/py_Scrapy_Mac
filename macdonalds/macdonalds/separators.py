def get_item_id(url):
    return url.split("/")[-1].split(".")[0]

if __name__ == "__main__":
    get_item_id("https://www.mcdonalds.com/ua/uk-ua/product/200148.html#accordion-29309a7a60-item-7d187854c5")
