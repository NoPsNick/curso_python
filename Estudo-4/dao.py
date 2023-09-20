from main import Professor, Diario
from conexao import Conexao
con = Conexao(mhost="", db="", usr="", pw="")


class DAO:
    professores_todos, professores_nome, professores_usuario = (
        "professores_todos", "professores_nome", "professores_usuario")
    diarios_todos, diarios_data, diarios_situacao, diarios_data_e_situacao = (
        "diarios_todos", "diarios_data", "diarios_situacao", "diarios_data_e_situacao")
    inserir_professores, inserir_diarios = "inserir_professores", "inserir_diarios"
    diarios_usuario = "diarios_usuario"

    tipos = {professores_todos: "professores_todos",
             professores_nome: "professores_nome",
             professores_usuario: "professores_usuario",
             diarios_todos: "diarios_todos",
             diarios_data: "diarios_data",
             diarios_situacao: "diarios_situacao",
             diarios_data_e_situacao: "diarios_data_e_situacao",
             diarios_usuario: "diarios_usuario",
             inserir_professores: "inserir_professores",
             inserir_diarios: "inserir_diarios"}

    def __init__(self, tipo: str, dados: str = None, dados_em_lista: list = None):
        self.tipo = tipo
        self.dados = dados
        self.dados_em_lista = dados_em_lista

    def _pegar_sql_por_nome(self):
        names = self.dados.replace(" ", "").split(",")
        if len(names) >> 1:
            sql_base = f"SELECT p.* FROM {Conexao.tabela_professores} " \
                       f"WHERE "
            nms = " OR ".join([f"p.nome = '{nome}'" for nome in names])
            sql = sql_base + nms
        else:
            sql = f"SELECT p.* FROM {Conexao.tabela_professores}"
        return sql

    def _pegar_sql_por_usuario(self):
        usuarios = self.dados.replace(" ", "").split(",")
        if len(usuarios) >> 1:
            sql_base = f"SELECT p.* FROM {Conexao.tabela_professores} " \
                       f"WHERE "
            nms = " OR ".join([f"p.usuario = '{usuario}'" for usuario in usuarios])
            sql = sql_base + nms
        else:
            sql = f"SELECT p.* FROM {Conexao.tabela_professores}"
        return sql

    def _pegar_sql_diario_por_usuario(self):
        usuarios = self.dados.replace(" ", "").split(",")
        if len(usuarios) >> 1:
            sql_base = f"SELECT p.* FROM {Conexao.tabela_diarios} " \
                       f"WHERE "
            nms = " OR ".join([f"p.usuario = '{usuario}'" for usuario in usuarios])
            sql = sql_base + nms
        else:
            sql = f"SELECT p.* FROM {Conexao.tabela_professores}"
        return sql

    def _pegar_sql_por_data(self):
        data = self.dados.replace(" ", "").split(",")
        if len(data) == 1:
            sql = f"SELECT p.* FROM {Conexao.tabela_diarios} " \
                  f"WHERE p.data = '{data[0]}'"
        elif len(data) == 2:
            sql = f"SELECT p.* FROM {Conexao.tabela_diarios} " \
                  f"WHERE p.data BETWEEN '{data[0]}' AND '{data[1]}'"
        else:
            sql = f"SELECT p.* from {Conexao.tabela_diarios}"
        return sql

    def _pegar_sql_por_situacao(self):
        situations = self.dados.replace(" ", "").split(",")
        if len(situations) >> 1:
            sqlbase = f"select p.* from {Conexao.tabela_diarios} " \
                      f"WHERE "

            sits = " OR ".join([f"p.situacao = '{Diario.situacoes[sit]}'" for sit in situations])
            sql = sqlbase + sits
        else:
            sql = f"SELECT p.* from {Conexao.tabela_diarios}"
        return sql

    def get(self) -> list | bool:
        if self.tipo == self.tipos[self.professores_todos]:
            sql = f"SELECT p.* FROM {Conexao.tabela_professores}"
            professorespegos = con.consultar(sql)
            profs = []
            try:
                for linha in professorespegos:
                    profs.append(Professor(linha[0], linha[1], linha[2], linha[3]))
            except:
                return False
            con.fechar()
            return profs

        elif self.tipo == self.tipos[self.professores_nome]:
            if self.dados:
                sql = self._pegar_sql_por_nome()
                professorespegos = con.consultar(sql)
                profs = []
                try:
                    for linha in professorespegos:
                        profs.append(Professor(linha[0], linha[1], linha[2], linha[3]))
                except:
                    return False

                con.fechar()
                return profs
            else:
                return False

        elif self.tipo == self.tipos[self.professores_usuario]:
            if self.dados:
                sql = self._pegar_sql_por_usuario()
                professorespegos = con.consultar(sql)
                profs = []
                try:
                    for linha in professorespegos:
                        profs.append(Professor(linha[0], linha[1], linha[2], linha[3]))
                except:
                    return False

                con.fechar()
                return profs
            else:
                return False

        elif self.tipo == self.tipos[self.diarios_usuario]:
            if self.dados:
                sql = self._pegar_sql_diario_por_usuario()
                diariospegos = con.consultar(sql)
                diars = []
                try:
                    for linha in diariospegos:
                        diars.append(Diario(linha[0], linha[1], linha[2], linha[3], linha[4]))
                except:
                    return False

                con.fechar()
                return diariospegos
            else:
                return False

        elif self.tipo == self.tipos[self.diarios_data]:
            if self.dados:
                sql = self._pegar_sql_por_data()
                diariospegos = con.consultar(sql)
                diars = []
                try:
                    for linha in diariospegos:
                        diars.append(Diario(linha[0], linha[1], linha[2], linha[3], linha[4]))
                except:
                    return False

                con.fechar()
                return diariospegos
            else:
                return False

        elif self.tipo == self.tipos[self.diarios_situacao]:
            if self.dados:
                sql = self._pegar_sql_por_situacao()
                diariospegos = con.consultar(sql)
                diars = []
                try:
                    for linha in diariospegos:
                        diars.append(Diario(linha[0], linha[1], linha[2], linha[3], linha[4]))
                except:
                    return False

                con.fechar()
                return diars
            else:
                return False

        elif self.tipo == self.tipos[self.diarios_data_e_situacao]:
            if self.dados and self.dados_em_lista:
                sql_data = self._pegar_sql_por_data()
                sql_situacao = " AND " + " OR ".join([f"p.situacao = '{Diario.situacoes[sit]}'"
                                                      for sit in self.dados_em_lista])
                sql = sql_data + sql_situacao
                diariospegos = con.consultar(sql)
                diars = []
                try:
                    for linha in diariospegos:
                        diars.append(Diario(linha[0], linha[1], linha[2], linha[3], linha[4]))
                except:
                    return False

                con.fechar()
                return diars
            else:
                return False

        elif self.tipo == self.tipos[self.diarios_todos]:
            sql = f"select p.* from {Conexao.tabela_diarios}"
            diariospegos = con.consultar(sql)
            diars = []
            try:
                for linha in diariospegos:
                    diars.append(Diario(linha[0], linha[1], linha[2], linha[3], linha[4]))
            except:
                return diars

            con.fechar()
            return diars

        elif self.tipo == self.tipos[self.inserir_diarios]:
            if self.dados_em_lista:
                try:
                    for diario in self.dados_em_lista:
                        sql = f"insert into {Conexao.tabela_diarios}" \
                              f"(titulo, texto, data, usuario, situacao) " \
                              f"values {diario}"
                        con.manipular(sql)
                        con.fechar()
                    return True
                except:
                    return False
            else:
                return False

        elif self.tipo == self.tipos[self.inserir_professores]:
            if self.dados_em_lista:
                try:
                    for professor in self.dados_em_lista:
                        sql = f"insert into {Conexao.tabela_professores}" \
                              f"(nome, adm, usuario, senha) " \
                              f"values {professor}"
                        con.manipular(sql)
                        con.fechar()
                    return True
                except:
                    return False
            else:
                return False


if __name__ == "__main__":
    situacao = ["aberto", "fechado"]
    situas = " OR ".join([f"p.situacao = '{Diario.situacoes[sit]}'" for sit in situacao])
    print(situas)
