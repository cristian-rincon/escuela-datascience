import scrapy


class QuotesSpider(scrapy.Spider):
    """
    docstring
    """
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        """
        docstring
        """
        with open('resultados.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
