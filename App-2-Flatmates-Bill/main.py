class Bill:
    """
    Objeto que possuí as informações sobre a conta, como total, e o período da conta.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Objeto que possuí as informações sobre o colega de apartamento que divide a conta.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        pass


class PdfReport:
    """
    Objeto que cria um arquivo pdf que possuí informações, como os colegas de apartamentos e seus nomes, o quanto eles
    pagaram e o período da conta.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass



