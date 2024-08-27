import scrapy


class DivDivanParsSpider(scrapy.Spider):
    name = "divDivanPars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru"]

    def parse(self, response):
        pass
