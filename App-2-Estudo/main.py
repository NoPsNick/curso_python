from datetime import datetime


class Dados:

    # Data,Horário,Usuário,Páginas,Cópias,Impressora,Arquivo,Tipo,
    # Tamanho,Tipo de Impressão,Estação,Duplex,Escala de Cinza.
    def __init__(self, dt, hor, usu, pag, cop, imp, arq, tip, tam, tip_da_imp, est, dup, esc_cinza):
        self.dup = dup
        self.est = est
        self.tip_da_imp = tip_da_imp
        self.tam = tam
        self.esc_cinza = esc_cinza
        self.tip = tip
        self.arq = arq
        self.imp = imp
        self.cop = cop
        self.pag = pag
        self.usu = usu
        self.dt = dt
        self.hor = hor


class Backup:

    def __init__(self, nome_do_arquivo):
        self.nome_do_arquivo = nome_do_arquivo

    def gerar_csv(self, listdados=None):
        if listdados is None:
            return False
        csv = open(f".\\impressoes\\{self.nome_do_arquivo}.csv", "w")
        csv.close()
        data = datetime.now().strftime('%d/%m/%Y')
        with open(f".\\impressoes\\{self.nome_do_arquivo}.csv", "a") as csv:
            csv.write(f"Relatório feito na data: {data}\n")
            for dado in listdados:
                csv.write(f"{dado.dt}, {dado.hor}, {dado.usu}, {dado.pag}, {dado.cop}, {dado.imp}, "
                          f"{dado.arq}, {dado.tip}, {dado.tam}, {dado.tip_da_imp}, {dado.est}, "
                          f"{dado.dup}, {dado.esc_cinza}\n")
            csv.close()
        return True


lista_de_dados = []
dado_1 = Dados(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
lista_de_dados.append(dado_1)
dado_2 = Dados(14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
lista_de_dados.append(dado_2)
impre = Backup("test")

