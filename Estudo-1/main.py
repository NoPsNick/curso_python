from backup import Backup
from leitura import Leitura

dados = Leitura().criar()
impre = Backup(dicionario=dados)

print(impre.gerar_csv())
print(impre.gerar_total())
