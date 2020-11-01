import scrapy
import datetime
from .common import config

TIME = datetime.datetime.now()
MEMUSAGE_NOTIFY_MAIL = str(
    config()['scraper']['intelligence_agency']['memusage_notify_mail'])
URL = str(config()['scraper']['intelligence_agency']['url'])
LINKS = str(config()['scraper']['intelligence_agency']['title_links'])
TITLE = str(config()['scraper']['intelligence_agency']['title'])
PARAGRAPH = str(config()['scraper']['intelligence_agency']['paragraph'])


class SpiderCIA(scrapy.Spider):
    """
    Clase principal del spider
    """
    name = 'cia'
    start_urls = [URL]
    # Settings to save in file
    custom_settings = {
        'FEED_URI': f'results/{name}_{TIME.strftime("%d-%b-%Y_%H-%M-%S")}.json',
        'FEED_FORMAT': 'json',
        'CONCURRENT_REQUESTS': 24,  # Number of concurrent requests
        'MEMUSAGE_LIMITS_MB': 2048,
        'MEMUSAGE_NOTIFY_MAIL': [MEMUSAGE_NOTIFY_MAIL],
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'CristianRincon',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        """
        Manejador de la respuesta
        """
        links_declassified = response.xpath(LINKS).getall()
        for link in links_declassified:
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})

    def parse_link(self, response, **kwargs):
        """
        docstring
        """
        link = kwargs['url']
        title = response.xpath(TITLE).get()
        paragraph = response.xpath(PARAGRAPH).get()

        yield {
            'url': link,
            'title': title,
            'body': paragraph
        }
