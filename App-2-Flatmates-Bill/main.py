from colega import Flatmate
from conta import Bill
from pdfreport import PdfReport

# Inputs pedidos para o usuário
# Conta
preco: float = float(input("O preço da conta: "))
periodo: str = input("O período da conta(por exemplo, Junho de 2023): ")

# Colegas de quarto
nome1: str = input("Seu nome: ")
dias_em_casa1: int = int(input("Os dias em que você ficou na casa: "))
nome2: str = input("Nome de seu colega: ")
dias_em_casa2: int = int(input(f"Os dias em que {nome2} ficou na casa: "))

# Criando os objetos
conta = Bill(amount=preco, period=periodo)
primeiro = Flatmate(name=nome1, days_in_house=dias_em_casa1)
segundo = Flatmate(name=nome2, days_in_house=dias_em_casa2)

# Mostrando os resultados
print(f"{primeiro.name} paga: ", primeiro.pays(bill=conta, flatmate2=segundo))
print(f"{segundo.name} paga: ", segundo.pays(bill=conta, flatmate2=primeiro))

# Gerando o PDF e o abrindo.
pdf_report = PdfReport(filename=f"{conta.period}.pdf")
pdf_report.generate(flatmate1=primeiro, flatmate2=segundo, bill=conta)
