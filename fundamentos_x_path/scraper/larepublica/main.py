import os
import datetime
import lxml.html as html
import requests
import yaml

# Utilites
from common import config

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

HOME_URL = str(config()['larepublica']['url'])
XPATH_LINK_TO_ARTICLE = str(config()['larepublica']['links'])
XPATH_TITLE = str(config()['larepublica']['titulo'])
XPATH_SUMMARY = str(config()['larepublica']['resumen'])
XPATH_BODY = str(config()['larepublica']['cuerpo'])


def error_handler():
    """
    docstring
    """
    pass


def parse_notice(link, today):
    """
    docstring
    """
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)
            try:
                title = parsed.xpath(XPATH_TITLE)
                title = title[2] if len(title) > 1 else title[0]
                title = title.replace('\"', '')
                logger.info(f'Título {title} obtenido')
                summary = parsed.xpath(XPATH_SUMMARY)[0]
                logger.info('Resumen obtenido')
                body = parsed.xpath(XPATH_BODY)
                logger.info('Cuerpo obtenido')
            except IndexError as ie:
                logger.error(ie)

            with open(f'{os.path.join(today,title)}.txt', 'w', encoding='utf-8') as output:
                output.write(title)
                output.write('\n\n')
                output.write(summary)
                output.write('\n\n')
                for p in body:
                    output.write(p)
                    output.write('\n')
        else:
            raise ValueError(f'Error: {response.status_code}')
    except Exception as e:
        logger.error(e)


def parse_home():
    """
    docstring
    """
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            logger.info(
                f'Obteniendo los links de las noticias de: {HOME_URL} \n')
            # logger.info(links_to_notices)
            today = datetime.date.today().strftime('%d-%m-%Y')
            if not os.path.isdir(today):
                os.mkdir(today)

            for link in links_to_notices:
                parse_notice(link, today)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except Exception as e:
        logger.error(e)


def run():
    """
    docstring
    """
    parse_home()


if __name__ == "__main__":
    run()
