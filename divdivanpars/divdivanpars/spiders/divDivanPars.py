import scrapy


class DivDivanParsSpider(scrapy.Spider):
    name = "divDivanPars"
    allowed_domains = ["divan.ru", "www.divan.ru"]  # Учет обеих форм записи сайта
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        divans = response.css('div._Ud0k')  # Основной контейнер товаров
        for divan in divans:
            yield {
                "name": divan.css("div.wYUX2 span::text").get(),  # Название товара
                "price": divan.css("div.pY3d2 span::text").get(),  # Цена товара
                "url": response.urljoin(divan.css("a").attrib["href"])  # Ссылка на товар
            }


# Запуск скрепинга следующей строкой через терминал
# scrapy crawl svet_pars -o result.csv -t csv