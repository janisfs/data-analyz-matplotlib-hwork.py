import scrapy


class DivDivanParsSpider(scrapy.Spider):
    name = "divDivanPars"
    allowed_domains = ["divan.ru", "www.divan.ru"]  # Учет обеих форм записи сайта
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        svets = response.css('div._Ud0k')  # Основной контейнер товаров
        for svet in svets:
            yield {
                "name": svet.css("div.wYUX2 span::text").get(),  # Название товара
                "price": svet.css("div.pY3d2 span::text").get(),  # Цена товара
                "url": response.urljoin(svet.css("a").attrib["href"])  # Ссылка на товар
            }