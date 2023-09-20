import math
from datetime import datetime


class Backup:
    """ Salva o dicionário dentro da classe e pode ser chamado para
    gerar o CSV com todos os nomes separados ou o total de folhas
    utilitazadas por cada pessoa retornando um dicionário com tais
    informações e criando os arquivos.
    """

    def __init__(self, dicionario: dict):
        self.dicionario = dicionario

    def _criar_arq_e_pegar_a_data_atual(self, tipo):
        for nome in self.dicionario.keys():
            if tipo == 'csv':
                csv = open(f".\\csvs\\{nome}.csv", "w")
                csv.close()
            elif tipo == 'total':
                csv = open(f".\\totais\\{nome}_total.csv", "w")
                csv.close()
        data = datetime.now().strftime('%d-%m-%Y')
        return data

    def gerar_csv(self):
        # Retorna falso caso não tenha nada salvo.
        if self.dicionario is None or self.dicionario == {}:
            return False
        # Pega a data atual e já cria os arquivos para escrita.
        data = self._criar_arq_e_pegar_a_data_atual(tipo="csv")
        # Para cada arquivo se cria um com o mesmo nome,
        # salvando neles os Dados.
        for dado in self.dicionario.keys():
            if self.dicionario[dado] is not []:
                with open(f".\\csvs\\{dado}.csv", "a") as csv:
                    csv.write(f"Relatório feito na data: {data}\n")
                    csv.write("Data, Horário, Usuário, Páginas,"
                              " Cópias, Impressora, Arquivo,"
                              " Tipo, Tamanho, Tipo de Impressão,"
                              " Estação, Duplex,Escala de Cinza\n")
                    for info in self.dicionario[dado]:
                        csv.write(f"{info.dt}, {info.hor}, "
                                  f"{info.usu}, {info.pag}, "
                                  f"{info.cop}, {info.imp}, "
                                  f"{info.arq}, {info.est}, "
                                  f"{info.dup}, {info.esc_cinza}\n")
                    csv.close()
        # Retorna o dicionário principal
        return self.dicionario

    def gerar_total(self):
        # Retorna falso caso não tenha nada salvo.
        if self.dicionario is None or self.dicionario == {}:
            return False
        # Pega a data atual e já cria os arquivos para escrita.
        data = self._criar_arq_e_pegar_a_data_atual(tipo='total')
        # Cria um arquivo contendo os nomes de todos e quantas
        # folhas foram utilizadas por cada.
        totais = {}
        for dado in self.dicionario.keys():
            if self.dicionario[dado] is not []:
                total = {}
                for num, pessoa in enumerate(self.dicionario[dado]):
                    if num == 0:
                        total[pessoa.usu] = 0
                    if str(pessoa.dup).lower() == "no":
                        # Total da pessoa = (páginas * cópias) + total antigo
                        total[pessoa.usu] += int(pessoa.pag) * int(pessoa.cop)
                    else:
                        # Total da pessoa = ((páginas * cópias)/2) + total antigo
                        total[pessoa.usu] += math.ceil(int(pessoa.pag) / 2) * int(pessoa.cop)
                with open(f".\\totais\\{dado}_total.csv", "w") as csv:
                    csv.write(f"Relatório total feito na data: {data}\n")
                    csv.write(f"Usuário, Total\n")
                    for pessoa in total:
                        csv.write(f"{pessoa}, {total[pessoa]}\n")
                        totais[pessoa] = total[pessoa]
                    csv.close()
                with open(f".\\csvs\\total_geral_{data}.csv", "w") as csv:
                    csv.write(f"Relatório total feito na data: {data}\n")
                    csv.write(f"Usuário, Total\n")
                    for pessoa in totais.keys():
                        csv.write(f"{pessoa}, {totais[pessoa]}\n")
                    csv.close()
        # Retorna um dicionário contendo o nome do usuario
        # ligado a quantas folhas ele utilizou.
        return totais
