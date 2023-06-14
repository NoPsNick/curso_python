import requests
from selectorlib import Extractor
from bs4 import BeautifulSoup
import requests
import os
import json

from noticias import Noticias


class Scrap:
    extractor_tipos = ["extractor", "ext"]
    beaultifulsoup_tipos = ["beaultifulsoup", "bs"]
    scrapy_tipos = ["scrapy", "scr"]

    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    base_url = 'https://agenciadenoticias.ibge.gov.br/'
    yml_path = 'datatextlink.yaml'
    aranha = "scrapy runspider ./scrapytype/scrapytype/spiders/agenciadenoticias.py -O noticias.json"

    def __init__(self, tipo):
        self.tipo = tipo.lower()

    def conteudo(self):
        r = requests.get(self.base_url, headers=self.headers)
        return r

    def tipo_beautifulsoup(self):
        soup = BeautifulSoup(self.conteudo().content, 'html.parser')
        news = soup.find(class_="pure-u-md-1-2 pure-u-1 home-nivel-1-direita")
        subnews = news.find_all('li')
        return subnews

    def tipo_extractor(self):
        extractor = Extractor.from_yaml_file(self.yml_path)
        raw_content = extractor.extract(self.conteudo().text)
        return raw_content

    def tipo_scrapy(self):
        os.system(self.aranha)
        try:
            with open("noticias.json", "r") as read_file:
                pegar = json.load(read_file)
        except:
            pegar = {}
        return pegar

    def get(self):
        noticias = []
        if self.tipo in self.extractor_tipos:
            scraped_content = self.tipo_extractor()
            for data, texto, link in zip(scraped_content['noticias']['datas'],
                                         scraped_content['noticias']['textos'],
                                         scraped_content['noticias']['links']):
                noticias.append(Noticias(data, texto, link))

            return noticias

        elif self.tipo in self.beaultifulsoup_tipos:
            scraped_content = self.tipo_beautifulsoup()
            noticias = []
            for num in range(len(scraped_content)):
                data = scraped_content[num].find(
                    class_='sidebar--agenda__data').get_text()
                data = data.replace("\n", "")
                data = data.replace("\r", "")
                data = data.strip()
                texto = scraped_content[num].find(
                    class_='sidebar--agenda__evento').get_text()
                texto = texto.replace("\n", "")
                texto = texto.replace("\r", "")
                texto = texto.strip()
                try:
                    link = scraped_content[num].find('a')['href']
                except:
                    link = "Esta notícia não há link."
                noticias.append(Noticias(data, texto, link))
            return noticias

        elif self.tipo in self.scrapy_tipos:
            pegar = self.tipo_scrapy()
            noticias = []
            for noticia in pegar:
                noticias.append(Noticias(noticia["data"],
                                         noticia["texto"],
                                         noticia["link"]))
            return noticias

        else:
            return print("Tipo de extração incorreto, tipos: ",
                         f"Extractor: {self.extractor_tipos}")

if __name__ == '__main__':
    noticias = Scrap("scR").get()
    for noticia in noticias:
        print(noticia.get())
