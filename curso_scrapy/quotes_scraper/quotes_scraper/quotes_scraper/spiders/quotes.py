import scrapy

# Utilites
from .common import config
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TITLE = str(config()['scraper']['quotes_scraper']['titulo'])
QUOTES = str(config()['scraper']['quotes_scraper']['citas'])
TOP_TAGS = str(config()['scraper']['quotes_scraper']['top_tags'])
NEXT_PAGE_BUTTON = str(
    config()['scraper']['quotes_scraper']['next_page_button'])


class QuotesSpider(scrapy.Spider):
    """
    docstring
    """
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]
    # Settings to save in file
    custom_settings = {
        'FEED_URI': f'results/{name}.json',
        'FEED_FORMAT': 'json'
    }

    def parse_only_quotes(self, response, **kwargs):
        """
        Parsear solo las citas.
        """
        if kwargs:
            quotes = kwargs['quotes']

        quotes.extend(response.xpath(QUOTES).getall())

        next_page_button_link = response.xpath(NEXT_PAGE_BUTTON).get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes})
        else:
            yield {'quotes': quotes}

    def parse(self, response):
        """
        Analizar un archivo para extraer información valiosa de él.
        """

        title = response.xpath(TITLE).get()
        quotes = response.xpath(QUOTES).getall()
        top_tags = response.xpath(TOP_TAGS).getall()

        top = getattr(self, 'top', None)

        if top:
            top = int(top)
            top_tags = top_tags[:top]

        yield {
            'title': title,
            'top_tags': top_tags
        }

        next_page_button_link = response.xpath(NEXT_PAGE_BUTTON).get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes})
