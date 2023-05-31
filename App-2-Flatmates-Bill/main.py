import webbrowser

from fpdf import FPDF


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

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Objeto que cria um arquivo pdf que possuí informações, como os colegas de apartamentos e seus nomes, o quanto eles
    pagaram e o período da conta.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Adicionando uma imagem
        pdf.image(name=".\\files\\house.png", w=30, h=30)

        # Inserindo o título
        pdf.set_font(family='Arial', size=14, style='B')
        pdf.cell(w=0, h=80, txt='Conta dos colegas de apartamento', border=1, align='C', ln=1)

        # Inserindo o período e o valor
        pdf.cell(w=100, h=40, txt='Período:', border=1)
        pdf.cell(w=100, h=40, txt=str(bill.period), border=1, ln=1)

        # Inserindo os colegas de quarto e quanto cada paga(ou)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=100, h=40, txt=flatmate1_pay, border=1, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=100, h=40, txt=flatmate2_pay, border=1, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)


conta = Bill(amount=120, period="Junho 2023")
francisco = Flatmate(name="Francisco", days_in_house=20)
felipe = Flatmate(name="Felipe", days_in_house=25)

print("Francisco paga: ", francisco.pays(bill=conta, flatmate2=felipe))
print("Felipe paga: ", felipe.pays(bill=conta, flatmate2=francisco))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=francisco, flatmate2=felipe, bill=conta)
