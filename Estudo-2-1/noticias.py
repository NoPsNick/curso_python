class Noticias:

    def __init__(self, data, texto, link):
        self.data = data
        self.texto = texto
        self.link = link

    def get(self):
        return f"{self.data}, {self.texto}, {self.link}"
