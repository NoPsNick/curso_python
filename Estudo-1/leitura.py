import os

from dados import Dados


class Leitura:
    """ Recebe o local de leitura, que recebe como base o caminho
    ".\\impressoes\\" e com isso efetua a leitura de todos
    os html no local, com isso podendo devolver um dicionário contendo as
    informações de cada.
    """

    _remover = ["\n", "<td>", "</td>", "<tr>", "</tr>",
                "</span>", "<title>PaperCut Print Logger : Print Logs - ",
                "</title>"]

    def __init__(self, localdeleitura: str = ".\\impressoes\\"):
        self.localdeleitura = localdeleitura

    def _ler(self):
        dados = {}
        for root, dirs, files in os.walk(self.localdeleitura, topdown=False):
            for name in files:
                nome = os.path.join(root, name)
                with open(nome, "r") as lendo:
                    # Lendo os arquivos e removendo informações desncessarias
                    ls = []
                    for line in lendo.readlines():
                        for remov in self._remover:
                            line = line.replace(remov, "")

                        ls.append(line.replace(
                            '<br /><span class="document_attrib">', ",")
                        )
                    lendo.close()
                dados[name] = ls
        return dados

    def criar(self):
        # Pegando as informações úteis
        dados = {}
        dicionarios = self._ler()
        for chave in dicionarios.keys():
            lista = []
            dat = dicionarios[chave][3]
            marcador = 74
            while 1:
                hor = dicionarios[chave][marcador]
                marcador += 1
                usu = dicionarios[chave][marcador]
                marcador += 1
                pag = dicionarios[chave][marcador]
                marcador += 1
                cop = dicionarios[chave][marcador]
                marcador += 1
                imp = dicionarios[chave][marcador]
                marcador += 1
                arq = dicionarios[chave][marcador]
                marcador += 1
                est = dicionarios[chave][marcador]
                marcador += 1
                dup = dicionarios[chave][marcador]
                marcador += 1
                esc_cinza = dicionarios[chave][marcador]
                lista.append(Dados(dat, hor, usu, pag, cop, imp, arq, est, dup, esc_cinza))
                if (marcador + 11) >= len(dicionarios[chave]):
                    break
                else:
                    marcador += 3
            dados[chave] = lista
        return dados
