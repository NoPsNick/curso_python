from random import randint


class Pessoa:

    def __init__(self, id, email, nome, usuario, senha):
        self.id = id
        self.email = email
        self.nome = nome
        self.usuario = usuario
        self.senha = senha

    def enviar_msg(self, ident, titulo, mensagem, destinatario):

        return Mensagem(id=ident, titulo=titulo, mensagem=mensagem, remetente=self, destinatario=destinatario)

    def pegar_msg(self, msgs):
        lista = []
        for msg in msgs:
            if msg.destinatario == self:
                lista.append(msg)
        return lista


class Mensagem:

    def __init__(self, id, titulo, mensagem, remetente, destinatario):
        self.id = id
        self.titulo = titulo
        self.mensagem = mensagem
        self.remetente = remetente
        self.destinatario = destinatario

    def get(self):
        identificador = self.id
        titulo = self.titulo
        mensagem = self.mensagem
        remetente = self.remetente
        return f"[{identificador}] {titulo}:\n" \
               f"{mensagem}\n" \
               f"Enviado por: {remetente.nome}."


pessoa1 = Pessoa(randint(1, 100), "email1", "francisco", "xico", "abc123")
pessoa2 = Pessoa(randint(1, 100), "email2", "felipe", "frufet", "123abc")

mensagem_da_pessoa1 = pessoa1.enviar_msg(randint(1, 100), "Titulo1", "mensagem1", pessoa2)
mensagem_da_pessoa2 = pessoa2.enviar_msg(randint(1, 100), "Titulo2", "mensagem2", pessoa1)
mensagem_da_pessoa1_2 = pessoa1.enviar_msg(randint(1, 100), "Titulo3", "mensagem3", pessoa2)
mensagem_da_pessoa2_2 = pessoa2.enviar_msg(randint(1, 100), "Titulo4", "mensagem4", pessoa1)

pegar = pessoa1.pegar_msg([mensagem_da_pessoa1, mensagem_da_pessoa2, mensagem_da_pessoa1_2, mensagem_da_pessoa2_2])
for msg in pegar:
    print(msg.get())
