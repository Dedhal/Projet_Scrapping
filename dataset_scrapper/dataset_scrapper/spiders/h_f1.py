import scrapy
from dataset_scrapper.items import DatasetScrapperItem

VISITED = []

class HF1Spider(scrapy.Spider):
    name = "h_f1"
    allowed_domains = ["hotelf1.accor.com"]
    start_urls = ["https://hotelf1.accor.com/"]

    def parse(self, response):
        global VISITED

        href = response.css("a::attr(href)").extract()
        
        if response.request.url in VISITED:
            return
        
        VISITED.append(response.request.url)

        yield DatasetScrapperItem(url=response.request.url, links=href)
        
        for link in href:
            yield scrapy.Request(link, callback=self.parse)
        
    