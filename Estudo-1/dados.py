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

    def __repr__(self):
        return str(self.__dict__)
