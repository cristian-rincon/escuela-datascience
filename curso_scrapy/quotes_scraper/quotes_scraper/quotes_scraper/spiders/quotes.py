import scrapy

# Utilites
from .common import config
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TITLE = str(config()['scraper']['quotes_scraper']['titulo'])
QUOTES = str(config()['scraper']['quotes_scraper']['citas'])
TOP_TEN_TAGS = str(config()['scraper']['quotes_scraper']['top_ten_tags'])


class QuotesSpider(scrapy.Spider):
    """
    docstring
    """
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/page/2/'
    ]

    def parse(self, response):
        """
        Analizar un archivo para extraer información valiosa de él.
        """

        title = response.xpath(TITLE).get()
        quotes = response.xpath(QUOTES).getall()
        top_ten_tags = response.xpath(TOP_TEN_TAGS).getall()

        yield {
            'title': title,
            'quotes': quotes,
            'top_ten_tags': top_ten_tags
        }