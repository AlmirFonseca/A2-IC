
from openpyxl import Workbook
from openpyxl.styles.alignment import Alignment
from openpyxl.drawing.image import Image
from openpyxl.utils import get_column_letter

import qrcodeGenerator

import random

# Translada a origem das linhas da tabela segundo o valor definido por "row_offset"
def row_adjust(row_value_without_offset):
    return row_value_without_offset + row_offset

# Translada a origem das colunas da tabela segundo o valor definido por "column_offset"
def col_adjust(column_value_without_offset):
    return column_value_without_offset + column_offset

# Cria um Workbook
wb = Workbook()

# Worksheet "Dashboard"
###############################################################################

# Aponta para a Worksheet ativa
ws = wb.active
# Acessa o atributo "title" da worksheet e o altera, renomeando a planilha
ws.title = "Dashboard"

# Para uma pessoa com 22 ações de 9.23 dólares da stone, que valem 22x9.23=203,06:
# E algo semelhante em relação à amazon
header = ["Nome", "Código/Ticker", "Tipo", "Quantidade", "Valor unitário", "Valor Total"]

# Lista das larguras de cada coluna da tabela
column_widths = [40, 15, 15, 15, 15, 15]

financial_data = [["StoneCro Ltd.", "STNE", "Ação", 22, 9.23, 203.06],
        ["Amazon.com, Inc", "AMZN", "Ação", 2, 2127.07, 4252.14]]

wallet_value = 186.45

# Define o número de linhas e colunas a serem "puladas" a partir do início da worksheet
row_offset = 1
column_offset = 1

# Cria o cabeçalho de uma tabela
ws.merge_cells(start_row=row_adjust(1), start_column=col_adjust(1), end_row=row_adjust(1), end_column=col_adjust(len(header))) # Merge as células imediatamente acima da tabela
ws.cell(row=row_adjust(1), column=col_adjust(1), value="Ativos") # Define o texto da célula
ws.cell(row=row_adjust(1), column=col_adjust(1)).alignment = Alignment(horizontal="center") # Centraliza o conteúdo

for head in header:
    ws.cell(row=row_adjust(2), column=col_adjust(header.index(head)+1), value=head)

# Transcreve uma lista de listas para a worksheet
for row_num, row_content in enumerate(financial_data):
    for data in row_content:
        ws.cell(row=row_adjust(row_num+3), column=col_adjust(row_content.index(data)+1), value=data)

# Ajusta a largura das colunas da tabela segundo os valores da lista "column_widths"
for i, column_width in enumerate(column_widths, col_adjust(1)):
    ws.column_dimensions[get_column_letter(i)].width = column_width
        
# Worksheet "QR Code"
###############################################################################
# Gera um QR Code a partir do "wallet_value" e retorna o caminho até o arquivo gerado
qrcode_path = qrcodeGenerator.gerar_qrcode(wallet_value)

# Cria uma nova Worksheet chamada "QR Code"
ws = wb.create_sheet(title="QR Code")

# Retira a exibição das linhas de grade
ws.sheet_view.showGridLines = False

# Imprime um texto na célula de coordenadas (2, 2) -> B2
ws.cell(2, 2, value= "Aponte a câmera do celular para o QR Code abaixo e confira o valor total da sua carteira:")

# Abre a imagem gerada que contém o QR code
img = Image(qrcode_path)

# Adiciona a imagem à tabela, ancorada sobre a célula de coordenadas (4, 3) -> C4
ws.add_image(img, ws.cell(4, 3).coordinate)

filename = "./rascunhos/Teste-" + str(random.randint(1, 10000)) + ".xlsx"
# Salva o arquivo
wb.save(filename)


# DECIDIR ENTRE OS DOIS MODELOS DE DICT E, CONSEQUENTEMENTE, ENTRE UM OUTPUT COM 1 OU 2 TABELAS
# PROTEGER A TABELA?
