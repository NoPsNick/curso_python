import scrapy


class AgenciadenoticiasSpider(scrapy.Spider):
    name = "agenciadenoticias"
    allowed_domains = ["agenciadenoticias.ibge.gov.br"]
    start_urls = ["https://agenciadenoticias.ibge.gov.br"]

    def parse(self, response, **kwargs):
        for noticia in response.css('div.destaque-nivel-3-content li'):
            yield {'data': noticia.css('div.sidebar--agenda__data::text').get().strip(),
                   'texto': noticia.css('div.sidebar--agenda__evento a::text').get().strip(),
                   'link': noticia.css('div.sidebar--agenda__evento a::attr("href")').get().strip()}
