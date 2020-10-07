import requests
from bs4 import BeautifulSoup

articles_list = ['/colombia/cali',
                 '/colombia/otras-ciudades/ultimas-noticias-murio-el-cantante-vallenato-miguel-duran-junior-por-coronavirus-535738',
                 '/colombia/santander/noticias-de-colombia-jose-eugenio-el-caricaturista-sin-cedula-que-incomoda-a-la-politica-535631',
                 '/contenido-comercial/entorno-abre-convocatoria-para-descubrir-emprendimientos-unicornios-535540',
                 '/colombia/cali/noticias-de-colombia-video-del-maltrato-a-una-zarigueeya-por-jovenes-en-el-valle-de-cauca-535827',
                 '/colombia/santander',
                 '/colombia/otras-ciudades/noticias-de-colombia-agente-de-transito-fue-multado-porque-no-su-moto-no-tenia-soat-535740',
                 '/colombia/otras-ciudades',
                 '/contenido-comercial',
                 '/colombia/otras-ciudades/por-segunda-vez-dimar-falla-hotel-las-americas-invade-la-playa-535795',
                 '/colombia/otras-ciudades/tunel-de-la-linea-protestas-en-la-via-la-linea-por-posibles-afectaciones-a-una-vereda-535772',
                 None]




def get_article_info(article_soup):

    info_dict = {}
    # Extracting Title
    title = article_soup.find('h1', attrs={'class': 'titulo'})
    if title:
        info_dict['title'] = title.text
    else:
        info_dict['title'] = None
    # Extracting volanta
    volanta = article_soup.find('p', attrs={'class': 'info'})
    if volanta:
        info_dict['volanta'] = volanta.text
    else:
        info_dict['volanta'] = None
    # Extracting date
    date = article_soup.find('span', attrs={'class': 'fecha'})
    if date:
        info_dict['date'] = date.text
    else:
        info_dict['date'] = None
    # Extracting Author
    author = article_soup.find('span', attrs={'class': 'nombre'})
    if author:
        info_dict['author'] = date.text
    else:
        info_dict['author'] = None
    # Extracting main image
    media_fig = article_soup.find(
        'figure', attrs={'class': 'foto-apertura-articulo'})
    images = media_fig.find_all('img')
    if len(images) == 0:
        print('No se encontraron imágenes')
    else:
        image = images[-1]
        img_src = image.get('data-original')
        if img_src:
            info_dict['image'] = img_src
    # Extracting text
    text = article_soup.find_all('p', attrs={'class': 'contenido'})
    info_dict['content'] = [t.text for t in text]

    return info_dict


def scrap_article(url_article):
    try:
        article = requests.get(url_article)
    except Exception as e:
        print('Error scrapeando la URL:', url_article)
        print(e)
        return None

    if article.status_code != 200:
        print(f'Error obteniendo artículo {url_article}')
        print(f'Status Code = {article.status_code}')
        return None

    article_soup = BeautifulSoup(article.text, 'lxml')

    result_dictionary = get_article_info(article_soup)
    result_dictionary['url'] = url_article

    return result_dictionary
