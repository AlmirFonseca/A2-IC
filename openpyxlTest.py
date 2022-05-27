
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
column_widths = [40, 15, 15, 15, 25, 25]

# Exemplo da estrutura de uma carteira
carteira = {
    "AMZN":{
        "ticker": "AMZN",
        "quantidade": 10,
        "tipo": "Ação",
        "nome": "Amazon.com, Inc.",
        "valor_unitario": 2221.55
    }, 
    "STNE":{
        "ticker": "STNE",
        "quantidade": 20,
        "tipo": "Ação",
        "nome": "StoneCo Ltd.",
        "valor_unitario": 9.71
    },   
    "BRL=X":{
        "ticker": "BRL=X",
        "quantidade": 1000,
        "tipo": "Moeda",
        "nome": "USD/BRL",
        "valor_unitario": 4.763
    }    
}

# Define o número de linhas e colunas a serem "puladas" a partir do início da worksheet
row_offset = 1
column_offset = 1

# Cria o cabeçalho de uma tabela
ws.merge_cells(start_row=row_adjust(1), start_column=col_adjust(1), end_row=row_adjust(1), end_column=col_adjust(len(header))) # Merge as células imediatamente acima da tabela
ws.cell(row=row_adjust(1), column=col_adjust(1), value="Ativos") # Define o texto da célula
ws.cell(row=row_adjust(1), column=col_adjust(1)).alignment = Alignment(horizontal="center") # Centraliza o conteúdo

# Preenche o cabeçalho da tabela a partir da lista "header"
for head in header:
    ws.cell(row=row_adjust(2), column=col_adjust(header.index(head)+1), value=head)

# Inicializa uma variável que acumulará o valor total da carteira
valor_total_carteira = 0

# Itera entre os ativos das certeiras
for row_num, data_ativo in enumerate(carteira.values(), 3):
    #Calcula o valor total referente a cada ativo e o adiciona ao dicionário
    valor_total_ativo = data_ativo.get("quantidade") * data_ativo.get("valor_unitario")
    data_ativo.update({"valor_total_ativo": valor_total_ativo})

    # Acumula o valor total da carteira
    valor_total_carteira += valor_total_ativo

    # Transcreve os itens do dicionario para a tabela, ajustando também o formato de exibição dos valores monetários
    ws.cell(row=row_adjust(row_num), column=col_adjust(1), value=data_ativo.get("nome"))
    ws.cell(row=row_adjust(row_num), column=col_adjust(2), value=data_ativo.get("ticker"))
    ws.cell(row=row_adjust(row_num), column=col_adjust(3), value=data_ativo.get("tipo"))
    ws.cell(row=row_adjust(row_num), column=col_adjust(4), value=data_ativo.get("quantidade"))
    ws.cell(row=row_adjust(row_num), column=col_adjust(5), value=round(data_ativo.get("valor_unitario"), 2)).number_format = "R$ #,###.00"
    ws.cell(row=row_adjust(row_num), column=col_adjust(6), value=round(data_ativo.get("valor_total_ativo"), 2)).number_format = "R$ #,###.00"

# Ajusta a largura das colunas da tabela segundo os valores da lista "column_widths"
for i, column_width in enumerate(column_widths, col_adjust(1)):
    ws.column_dimensions[get_column_letter(i)].width = column_width

# Prepara a última linha da tabela
ws.merge_cells(start_row=row_adjust(len(carteira)+3), start_column=col_adjust(1), end_row=row_adjust(len(carteira)+3), end_column=col_adjust(len(header)-1)) # Merge as células imediatamente acima da tabela
ws.cell(row=row_adjust(len(carteira)+3), column=col_adjust(1), value="Valor total da carteira") # Define o texto da célula
ws.cell(row=row_adjust(len(carteira)+3), column=col_adjust(1)).alignment = Alignment(horizontal="center") # Centraliza o conteúdo

# Imprime o valor total da carteira
ws.cell(row=row_adjust(len(carteira)+3), column=col_adjust(len(header)), value=round((valor_total_carteira), 2)).number_format = "R$ #,###.00"
        
# Worksheet "QR Code"
###############################################################################
# Gera um QR Code a partir do "valor_total_carteira" e retorna o caminho até o arquivo gerado
qrcode_path = qrcodeGenerator.gerar_qrcode(valor_total_carteira)

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
