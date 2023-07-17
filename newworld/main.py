import requests
from bs4 import BeautifulSoup
import json


class Scrap:

    def __init__(self, tipo):
        self.tipo = tipo.lower()

    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    base_url = 'https://nwdb.info/server-status/servers_24h.json'

    def conteudo(self):
        r = requests.get(self.base_url, headers=self.headers)
        return r

    def extrair(self):
        soup = BeautifulSoup(self.conteudo().text, 'html.parser')
        dicionario = json.loads(soup.get_text())
        if self.tipo == "sa":
            for servidor in dicionario["data"]['servers']:
                if servidor[6] == "sa-east-1":
                    print(f"{servidor[4]} > {servidor[1]}/{servidor[0]}")
        elif self.tipo == "all":
            for servidor in dicionario["data"]['servers']:
                print(f"{servidor[4]} > {servidor[1]}/{servidor[0]}")
        return dicionario


if __name__ == '__main__':
    noticias = Scrap("all").extrair()
