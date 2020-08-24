import scrapy

#XPath

# links = '//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href'
# title = '//div[@class="documentContent"]/h1[@class="documentFirstHeading"]/text()'
# body = '//div[@class="field-item even"]/p/text()'

class SpiderCIA(scrapy.Spider):
    name = 'cia'
    start_urls = [
        'https://www.cia.gov/library/readingroom/historical-collections'
    ]
    custom_settings = {
        'FEED_URI': 'cia.json',
        'FEED_FORMAT': 'json',
        'CONCURRENT_REQUEST': 24,
        'MEMUSAGE_LIMIT_MB': 2048,
        'MEMUSAGE_NOTIFY_MAIL': ['ing.oscarp1@gmail.com'],
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'Data Science Student Oscar Palomino',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
    def parse(self, response):
        links_declassified = response.xpath('//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href').getall()
        for link in links_declassified:
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})

    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath('//div[@class="documentContent"]/h1[@class="documentFirstHeading"]/text()').get()
        paragraph = response.xpath('//div[@class="field-item even"]/p[not(@class)]/text()').getall()
        yield {
            'url': link,
            'title': title,
            'body': paragraph
        }