from typing import Any

from datetime import datetime


class Dados:
    # Data,Horário,Usuário,Páginas,Cópias,Impressora,Arquivo,Tipo,
    # Tamanho,Tipo de Impressão,Estação,Duplex,Escala de Cinza.
    def __init__(self, dt, hor, usu, pag, cop, imp, arq, est, dup, esc_cinza):
        self.dt = dt
        self.hor = hor
        self.usu = usu
        self.pag = pag
        self.cop = cop
        self.imp = imp
        self.arq = arq
        self.est = est
        self.dup = dup
        self.esc_cinza = esc_cinza


class Leitura:

    def __init__(self, local):
        self.local = local

    # noinspection PyStatementEffect
    def ler(self):
        linhas = []
        with open(f"{self.local}", "r") as lendo:
            # Lendo o arquivo
            for line in lendo.readlines():
                linhas.append(line)

            # Removendo informação inútil
            for n, line in enumerate(linhas):
                linhas[n] = linhas[n].replace("\n", "")
                linhas[n] = linhas[n].replace("<td>", "")
                linhas[n] = linhas[n].replace("</td>", "")
                linhas[n] = linhas[n].replace("<tr>", "")
                linhas[n] = linhas[n].replace("</tr>", "")
                linhas[n] = linhas[n].replace('<br /><span class="document_attrib">', ",")
                linhas[n] = linhas[n].replace("</span>", "")
                linhas[n] = linhas[n].replace("<title>PaperCut Print Logger : Print Logs - ", "")
                linhas[n] = linhas[n].replace("</title>", "")
            lendo.close()

        return linhas

    def criar(self):
        # Pegando as informações úteis
        linhas = self.ler()
        dat = linhas[3]
        lista = []
        marcador = 75
        while 1:
            hor = linhas[marcador]
            marcador += 1
            usu = linhas[marcador]
            marcador += 1
            pag = linhas[marcador]
            marcador += 1
            cop = linhas[marcador]
            marcador += 1
            imp = linhas[marcador]
            marcador += 1
            arq = linhas[marcador]
            marcador += 1
            est = linhas[marcador]
            marcador += 1
            dup = linhas[marcador]
            marcador += 1
            esc_cinza = linhas[marcador]
            lista.append(Dados(dat, hor, usu, pag, cop, imp, arq, est, dup, esc_cinza))
            if (marcador+11) >= len(linhas):
                break
            else:
                marcador += 3

        return lista


class Backup:

    def __init__(self, nome_do_arquivo):
        self.nome_do_arquivo = nome_do_arquivo.replace('.csv', '')

    def gerar_csv(self, listdados=None):
        if listdados is None:
            return False
        csv = open(f".\\impressoes\\{self.nome_do_arquivo}.csv", "w")
        csv.close()
        data = datetime.now().strftime('%d/%m/%Y')
        with open(f".\\impressoes\\{self.nome_do_arquivo}.csv", "w") as csv:
            csv.write(f"Relatório feito na data: {data}\n")
            csv.write("Data, Horário, Usuário, Páginas, Cópias, Impressora, Arquivo, Tipo, Tamanho, Tipo de Impressão,"
                      " Estação, Duplex,Escala de Cinza\n")
            for info in listdados:
                csv.write(f"{info.dt}, {info.hor}, {info.usu}, {info.pag}, {info.cop}, {info.imp}, "
                          f"{info.arq}, {info.est}, "
                          f"{info.dup}, {info.esc_cinza}\n")
            csv.close()
        return True


dado = Leitura(str(input("Local do arquivo para leitura: "))).criar()
impre = Backup(str(input("Nome do arquivo para salvar: ")))
impre.gerar_csv(dado)
