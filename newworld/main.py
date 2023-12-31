import requests
import re


class Scrap:
    """ Pega o conteúdo do link https://nwdb.info/server-status/servers_24h.json
    e o transforma em dicionário do python para poder devolver
    as informações pedidas. Coloque a região que deseja ou
    all para todos, podendo colocar eles separados por vírgula","
    com o espaço trocado por "-".
    Exemplos: "sa-east, us-east", "eu, sa"...
    """

    def __init__(self, regioes):
        self.regioes = regioes.lower().replace(" ", "")

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

    def _conteudo(self) -> dict:
        r = requests.get(self.base_url, headers=self.headers)
        dicionario = r.json()
        return dicionario

    @staticmethod
    def _remover_numeros(dado):
        numbers = re.findall("[0-9]", dado)
        for num in numbers:
            dado = dado.replace(f"-{num}", "")
        return dado

    def extrair(self):
        texto = ""
        dicionario = self._conteudo()
        if self.regioes == "all":
            for servidor in dicionario["data"]['servers']:
                # Remover os números agora é desnecessário, mas deixei para estudo mesmo.
                texto += f"{self._remover_numeros(servidor[6])}: {servidor[4]} > {servidor[1]}/{servidor[0]}\n"
        else:
            for servidor in dicionario["data"]['servers']:
                # Remover os números agora é desnecessário, mas deixei para estudo mesmo.
                regiao = self._remover_numeros(servidor[6])
                for reg in self.regioes.split(","):
                    if re.search(f"^{reg}".lower(), servidor[6]):
                        texto += f"{regiao}: {servidor[4]} > {servidor[1]}/{servidor[0]}\n"
        return texto


if __name__ == '__main__':
    noticias = Scrap("sa, eu").extrair()
    print(noticias)

