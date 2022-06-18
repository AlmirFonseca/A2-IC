import os
from scrapping import constroi_objeto_carteira
from feat_yfinance import analisar_carteira, obter_historico_ativos, converter_valores_BRL
from openpyxl_generator import gerar_xlsx
from interface import cabecalho, entrada_url

# Imprime um cabeçalho no terminal
print(cabecalho)

# Função que recebe a entrada de uma url, e checa se a url é válida. Se sim, retorna-a
url = entrada_url()

# Função para construir a carteira e retorna dicionário com papéis e quantidades a partir de link do site.
carteira = constroi_objeto_carteira(url)

# Funções que trata os valores e identifica a exibição de ativos em moedas estrangeiras
carteira, tipos_moedas_estrangeiras = analisar_carteira(carteira)

# Caso, após a análise, não restem ativos válidos na carteira
if len(carteira) == 0:
    print("Não foram reconhecidos ativos válidos na carteira. Nenhum resultado foi produzido.")
else:
    # Funções que constroe o histórico de valores dos ativos a partir da lib yfinance
    historico_carteira = obter_historico_ativos(carteira)
    
    # Caso haja ativos exibidos em alguma moeda estrangeira, é necessário converter os valores para a moeda brasileira, o Real (BRL)
    if len(tipos_moedas_estrangeiras) > 0:
        converter_valores_BRL(carteira, historico_carteira, tipos_moedas_estrangeiras)

    #Função que gera os resultados a partir da carteira atual e do histórico gerado anteriormente.
    caminho_arquivo_resultados = gerar_xlsx(carteira, historico_carteira)
    
    # Imprime o local onde está salvo o arquivo gerado a partir da análise da carteira
    print("Os resultados da análise da sua carteira foram gerados e se encontram em:", caminho_arquivo_resultados, sep="\n")
    
    # Abre o arquivo de resultados gerado pela função anterior
    os.startfile(caminho_arquivo_resultados)