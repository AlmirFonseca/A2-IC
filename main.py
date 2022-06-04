import os
from scrapping import constroi_objeto_carteira
from feat_yfinance import analisar_carteira, obter_historico_ativos, converter_valores_BRL
from openpyxl_generator import gerar_xlsx

# Aguarda a inserção de uma url com a carteira de ativos a ser analisada
url = str(input('Digite o url da carteira desejada: \n'))

# Função para construir a carteira e retorna dicionário com papéis e quantidades a partir de link do site.
carteira = constroi_objeto_carteira(url)

# Funções que trata os valores e identifica a exibição de ativos em moedas estrangeiras
carteira, tipos_moedas_estrangeiras = analisar_carteira(carteira)

# Caso, após a análise, não restem ativos válidos na carteira
if len(carteira) == 0:
    print("Não há ativos válidos na carteira, sem retorno nos Resultados.")
else:
    # Funções que constroe o histórico de valores dos ativos a partir da lib yfinance
    historico_carteira = obter_historico_ativos(carteira)
    
    # Caso haja ativos exibidos em alguma moeda estrangeira, é necessário converter os valores para a moeda brasileira, o Real (BRL)
    if len(tipos_moedas_estrangeiras) > 0:
        converter_valores_BRL(carteira, historico_carteira, tipos_moedas_estrangeiras)

    #Função que gera os resultados a partir da carteira atual e do histórico gerado anteriormente.
    caminho_arquivo_resultados = gerar_xlsx(carteira, historico_carteira)
    
    # Abre o arquivo de resultados gerado pela função anterior
    #os.startfile(caminho_arquivo_resultados)