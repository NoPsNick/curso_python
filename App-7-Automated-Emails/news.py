# 32fe1b8ceba14ce082f804cd2f8a3c69
import requests


class NewsFeed:

    base_url = "https://newsapi.org/v2/everything?"
    api_key = "&apiKey=32fe1b8ceba14ce082f804cd2f8a3c69"

    def __init__(self, interest, fromdata, todata, language):
        self.interest = interest
        self.fromdata = fromdata
        self.todata = todata
        self.language = language

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}" \
              f"&from={self.fromdata}" \
              f"&to={self.todata}" \
              f"&language={self.language}" \
              f"{self.api_key}"
        return url

    def _get_request(self) -> dict:
        url = self._build_url()
        resposta = requests.get(url)
        conteudo = resposta.json()
        return conteudo

    def get(self):
        noticias = self._get_request()
        email_body = ''
        for noticia in noticias['articles']:
            email_body += noticia["title"] + "\n" + noticia["url"] + "\n\n"
        return email_body


if __name__ == '__main__':
    news_feed = NewsFeed("furtos", "2023-06-15", "2023-06-20", "pt")
    print(news_feed.get())
