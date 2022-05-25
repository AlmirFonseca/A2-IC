from openpyxl import Workbook
import random

# Cria um Workbook
wb = Workbook()

# Aponta para a Worksheet ativa
ws = wb.active
# Acessa o atributo "title" da worksheet e o altera, renomeando a planilha
ws.title = "Dashboard"



# Dados podem ser atribuídos diretamente às células
ws['A1'] = 42


# Linhas também podem ser acrescentadas
ws.append([1, 2, 3])

# Python types will automatically be converted
import datetime
ws['A2'] = datetime.datetime.now()

# Save the file
filename = "./rascunhos/Teste-" + str(random.randint(1, 10000)) + ".xlsx"
wb.save(filename)
