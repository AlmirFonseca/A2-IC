from openpyxl import Workbook
from openpyxl.styles.alignment import Alignment

import random

# Cria um Workbook
wb = Workbook()

# Aponta para a Worksheet ativa
ws = wb.active
# Acessa o atributo "title" da worksheet e o altera, renomeando a planilha
ws.title = "Dashboard"

# Para uma pessoa com 22 ações de 9.23 dólares da stone, que valem 22x9.23=203,06:
# E algo semelhante em relação à amazon
header = ["Nome", "Código/Ticker", "Quantidade", "Valor unitário", "Valor Total"]

financial_data = [["StoneCro Ltd.", "STNE", 22, 9.23, 203.06],
        ["Amazon.com, Inc", "AMZN", 2, 2127.07, 4252.14]]

# Define o número de linhas e colunas a serem "puladas" a partir do início da worksheet
row_offset = 1
column_offset = 1

# Cria o cabeçalho de uma tabela
ws.merge_cells(start_row=row_offset+1, start_column=column_offset+1, end_row=row_offset+1, end_column=column_offset+len(header)) # Merge as células imediatamente acima da tabela
ws.cell(row=row_offset+1, column=column_offset+1, value="Ativos") # Define o texto da célula
ws.cell(row=row_offset+1, column=column_offset+1).alignment = Alignment(horizontal="center") # Centraliza o conteúdo

for head in header:
    ws.cell(row=row_offset+2, column=header.index(head)+column_offset+1, value=head)

# Transcreve uma lista de listas para a worksheet
for row_num, row_content in enumerate(financial_data):
    for data in row_content:
        ws.cell(row=row_num+row_offset+3, column=row_content.index(data)+column_offset+1, value=data)

filename = "./rascunhos/Teste-" + str(random.randint(1, 10000)) + ".xlsx"
# Salva o arquivo
wb.save(filename)


# DECIDIR ENTRE OS DOIS MODELOS DE DICT E, CONSEQUENTEMENTE, ENTRE UM OUTPUT COM 1 OU 2 TABELAS
