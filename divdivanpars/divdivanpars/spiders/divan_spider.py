import scrapy

class DivanSpider(scrapy.Spider):  # Имя класса изменено
    name = "divan_spider"  # Имя паука изменено
    allowed_domains = ["divan.ru", "www.divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        divans = response.css('div._Ud0k')
        for divan in divans:
            yield {
                "name": divan.css("div.wYUX2 span::text").get(),
                "price": divan.css("div.pY3d2 span::text").get(),
                "url": response.urljoin(divan.css("a").attrib["href"])
            }


# Запуск скрепинга следующей строкой через терминал
# scrapy crawl divan_spider -o result.csv -t csv