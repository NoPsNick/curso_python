import webbrowser
import os

from fpdf import FPDF


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
        total = str(bill.amount)

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Adicionando uma imagem
        pdf.image(name=".\\files\\house.png", w=30, h=30)

        # Inserindo o título
        pdf.set_font(family='Arial', size=14, style='B')
        pdf.cell(w=0, h=80, txt='Conta dos colegas de apartamento', border=1, align='C', ln=1)

        # Inserindo o período da conta
        pdf.cell(w=100, h=40, txt='Período:', border=1)
        pdf.cell(w=0, h=40, txt=str(bill.period), border=1, ln=1)

        # Inserindo os colegas de quarto e quanto cada paga(ou)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=0, h=40, txt=flatmate1_pay, border=1, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=0, h=40, txt=flatmate2_pay, border=1, ln=1)

        # Total da conta
        pdf.cell(w=120, h=40, txt="Total da conta:", border=1)
        pdf.cell(w=0, h=40, txt=total, border=1, ln=1)

        # Alterando o diretório, criando o pdf e o abrindo
        os.chdir("pdfs")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
