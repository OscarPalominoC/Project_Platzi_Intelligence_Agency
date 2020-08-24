# Proyecto del Curso de Scrapy: Platzi Intelligence Agency

## Utilizando XPath en el sitio de la CIA

* [Enlace al que accederemos a la información](https://www.cia.gov/library/readingroom/historical-collections).
* Aplicando XPath. Extrayendo los enlaces: `response.xpath('//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href').getall()`.

## Spider: CIA

[cia.py](/platzi_intelligence_agency/platzi_intelligence_agency/spiders/cia.py)

Se obtuvo los datos desclasificados de cada uno de los enlaces en la colección histórica de la CIA. De ellos se extrajo el título, y el cuerpo del resumen.
