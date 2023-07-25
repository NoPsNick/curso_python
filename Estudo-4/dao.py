from main import Professor, Diario
from conexao import Conexao
con = Conexao(mhost="", db="", usr="", pw="")


class DAO:

    def __init__(self, professores_pegos=None, diarios_pegos=None):
        self.professores_pegos = professores_pegos
        self.diarios_pegos = diarios_pegos

    @staticmethod
    def _pegar_sql_por_nome(nomes):
        if nomes.len() >> 1:
            sql_base = f"SELECT p.* FROM {Conexao.tabela_professores} " \
                       f"WHERE "
            names = nomes.replace(" ", "").split(",")
            nms = " OR ".join([f"p.nome = '{nome}'" for nome in names])
            sql = sql_base + nms
        else:
            sql = f"SELECT p.* FROM {Conexao.tabela_professores}"
        return sql

    @staticmethod
    def _pegar_sql_por_usuario(usuarios):
        if usuarios.len() >> 1:
            sql_base = f"SELECT p.* FROM {Conexao.tabela_professores} " \
                       f"WHERE "
            users = usuarios.replace(" ", "").split(",")
            nms = " OR ".join([f"p.usuario = '{usuario}'" for usuario in users])
            sql = sql_base + nms
        else:
            sql = f"SELECT p.* FROM {Conexao.tabela_professores}"
        return sql

    @staticmethod
    def _pegar_sql_por_data(datas):
        data = datas.replace(" ", "").split(",")
        if data.len() == 1:
            sql = f"SELECT p.* FROM {Conexao.tabela_diarios} " \
                  f"WHERE p.data = '{data[0]}'"
        elif data.len() == 2:
            sql = f"SELECT p.* FROM {Conexao.tabela_diarios} " \
                  f"WHERE p.data BETWEEN '{data[0]}' AND '{data[1]}'"
        else:
            sql = f"SELECT p.* from {Conexao.tabela_diarios}"
        return sql

    @staticmethod
    def _pegar_sql_por_situacao(situacoes):
        situations = situacoes.replace(" ", "").split(",")
        if situations.len() >> 1:
            sqlbase = f"select p.* from {Conexao.tabela_diarios} " \
                      f"WHERE "

            sits = " OR ".join([f"p.situacao = '{Diario.situacoes[sit]}'" for sit in situations])
            sql = sqlbase + sits
        else:
            sql = f"SELECT p.* from {Conexao.tabela_diarios}"
        return sql

    def pegar_todos_professores(self):
        sql = f"SELECT p.* FROM {Conexao.tabela_professores}"
        professorespegos = con.consultar(sql)
        profs = []
        try:
            for linha in professorespegos:
                profs.append(Professor(linha[0], linha[1], linha[2], linha[3]))
        except:
            self.professores_pegos = None
            return False

        con.fechar()
        self.professores_pegos = profs
        return True

    def pegar_professores_por_nome(self, nomes):
        sql = self._pegar_sql_por_nome(nomes)
        professorespegos = con.consultar(sql)
        profs = []
        try:
            for linha in professorespegos:
                profs.append(Professor(linha[0], linha[1], linha[2], linha[3]))
        except:
            self.professores_pegos = None
            return False

        con.fechar()
        self.professores_pegos = profs
        return True

    def pegar_professores_por_usuario(self, usuarios):
        sql = self._pegar_sql_por_usuario(usuarios)
        professorespegos = con.consultar(sql)
        profs = []
        try:
            for linha in professorespegos:
                profs.append(Professor(linha[0], linha[1], linha[2], linha[3]))
        except:
            self.professores_pegos = None
            return False

        con.fechar()
        self.professores_pegos = profs
        return True

    def pegar_diarios_por_data(self, datas):
        sql = self._pegar_sql_por_data(datas)
        diariospegos = con.consultar(sql)
        diars = []
        try:
            for linha in diariospegos:
                diars.append(Diario(linha[0], linha[1], linha[2], linha[3], linha[4]))
        except:
            self.diarios_pegos = None
            return False

        con.fechar()
        self.diarios_pegos = diars
        return True

    def pegar_diarios_por_situacao(self, situacoes):
        sql = self._pegar_sql_por_situacao(situacoes)
        diariospegos = con.consultar(sql)
        diars = []
        try:
            for linha in diariospegos:
                diars.append(Diario(linha[0], linha[1], linha[2], linha[3], linha[4]))
        except:
            self.diarios_pegos = None
            return False

        con.fechar()
        self.diarios_pegos = diars
        return True

    def pegar_diarios_por_data_e_situacao(self, datas, situacoes):
        sql_data = self._pegar_sql_por_data(datas)
        sql_situacao = " AND " + " OR ".join([f"p.situacao = '{Diario.situacoes[sit]}'"
                                              for sit in situacoes])
        sql = sql_data + sql_situacao
        diariospegos = con.consultar(sql)
        diars = []
        try:
            for linha in diariospegos:
                diars.append(Diario(linha[0], linha[1], linha[2], linha[3], linha[4]))
        except:
            self.diarios_pegos = None
            return False

        con.fechar()
        self.diarios_pegos = diars
        return True

    def pegar_todos_diarios(self):
        sql = f"select p.* from {Conexao.tabela_diarios}"
        diariospegos = con.consultar(sql)
        diars = []
        try:
            for linha in diariospegos:
                diars.append(Diario(linha[0], linha[1], linha[2], linha[3], linha[4]))
        except:
            self.diarios_pegos = None
            return False

        con.fechar()
        self.diarios_pegos = diars
        return True

    def inserir_diarios(self):
        try:
            for diario in self.diarios_pegos:
                sql = f"insert into {Conexao.tabela_diarios}" \
                      f"(titulo, texto, data, usuario, situacao) " \
                      f"values {diario}"
                con.manipular(sql)
                con.fechar()
            return True
        except:
            return False

    def inserir_professores(self):
        try:
            for professor in self.professores_pegos:
                sql = f"insert into {Conexao.tabela_professores}" \
                      f"(nome, adm, usuario, senha) " \
                      f"values {professor}"
                con.manipular(sql)
                con.fechar()
            return True
        except:
            return False


if __name__ == "__main__":
    situacao = ["aberto", "fechado"]
    situas = " OR ".join([f"p.situacao = '{Diario.situacoes[sit]}'" for sit in situacao])
    print(situas)
