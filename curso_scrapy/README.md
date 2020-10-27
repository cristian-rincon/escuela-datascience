# Curso de Scrapy

## Qué es Scrapy

Framework de alto nivel para realizar

- web scraping
- web crawling (capturar los links de una página para indexarlos y llegar a un nuvo sitio)

> Scrapy es Asíncrono

## Herramientas

- Procesador de XPath
- Interactive Shell
- se pueden exportar los archivos en JSON,CSV, etc.
- Respeta el archivo robots.txt, no es necesario controlarlo, ya lo hace el framework.

## Crear proyecto con scrapy

```python
scrapy startproject tutorial
# Run
scrapy startproject tutorial
```

## Generadores - yield = return parcial

Una función con 'poderes' especiales. En una función, python guarda el estado de la función para cuando la volvamos a necesitar y retomar.

## Iterables

A partir de ellos puedo crear un objeto de tipo iterador, para poder recorrer elemento por elemento en un ciclo

## Consola interactiva de scrapy

```bash
scrapy shell 'https://quotes.toscrape.com/page/2/'
response.xpath('//h1/a/text()')
response.xpath('//h1/a/text()').get() # trae un solo elemento
response.xpath('//span[@class="text"]/text()').getall() # trae todos los elementos que cumplan las condiciones
```

## Exportar resultados scrapy

```bash
scrapy crawl quotes -o results/quotes.json
```

## Spiders

Clase de python en la que creamos la lógica para extraer información
