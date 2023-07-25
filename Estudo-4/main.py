class Professor:

    def __init__(self, nome: str, adm: bool, usuario: str, senha: str):
        self.nome = nome
        self.adm = adm
        self.usuario = usuario
        self.senha = senha

    def __repr__(self):
        return str(self.__dict__)

    def criar_diario(self, titulo, texto):
        novo_diario = Diario(titulo=titulo,
                             texto=texto,
                             data="agora",
                             usuario=self.usuario,
                             situacao=Diario.situacoes[Diario.Aberto])
        novo_diario.salvar()
        return novo_diario

    def ver_diarios(self, situacoes=None, datas=None):
        pass


class Diario:
    Aberto, Fechado, Removido = "aberto", "fechado", "removido"
    situacoes = {Aberto: "aberto", Fechado: "fechado", Removido: "removido"}

    def __init__(self, titulo: str, texto: str, data, usuario: str, situacao: str):
        self.titulo = titulo
        self.texto = texto
        self.data = data
        self.usuario = usuario
        self.situacao = situacao

    def __repr__(self):
        return str(self.__dict__)

    def salvar(self):
        pass

    def alterar_situacao(self, situacao):
        self.situacao = self.situacoes[situacao]
        self.salvar()
        return self

    def escrever(self):
        return f"Diário feito por: {self.usuario}\n" \
               f"Título: {self.titulo}\n" \
               f"Texto: {self.texto}\n" \
               f"Data: {self.data}\n" \
               f"Situação: {self.situacao}\n"


if __name__ == "__main__":
    prof = Professor("Francisco", True, "francisco", "123")
    diariocriado = prof.criar_diario("Teste", "Texto grande.")
    print(diariocriado.escrever())
    diariocriado = diariocriado.alterar_situacao(Diario.Fechado)
    print(diariocriado.escrever())
