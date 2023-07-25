import psycopg2 as psycopg2


class Conexao:
    _db = None
    tabela_professores = "tb_professores"
    tabela_diarios = "tb_diarios"

    def __init__(self, mhost, db, usr, pw):
        self._db = psycopg2.connect(
            host=mhost, database=db, user=usr,  password=pw)

    def manipular(self, sql):
        try:
            cur = self._db.cursor()
            cur.execute(sql)
            cur.close()
            self._db.commit()
        except:
            return False
        return True

    def consultar(self, sql):
        try:
            cur = self._db.cursor()
            cur.execute(sql)
            rs = cur.fetchall()
        except:
            rs = None
            return rs
        return rs

    def proxima_pk(self, tabela, chave):
        sql = f'select max({chave}) from {tabela}'
        rs = self.consultar(sql)
        pk = rs[0][0]
        return pk+1

    def fechar(self):
        self._db.close()
