from scrapping import constroi_objeto_carteira
from feat_yfinance import analisar_carteira, obter_historico_ativos
from openpyxl_generator import gerar_xlsx

# Função para construir a carteira e retorna dicioário com papéis e quantidades a partir de link do site.
url = str(input('Digite o url da carteira desejada \n'))
print(url)
carteira = constroi_objeto_carteira(url)

# Funções que tratam os valores e constroem o histórico dos ativos a partir da lib yfinance
analisar_carteira(carteira)
if len(carteira) == 0:
    print("Não há ativos válidos na carteira, sem retorno nos Resultados.")
else:
    historico_carteira = obter_historico_ativos(carteira)

    #Função que gera os resultados a partir da carteira atual e do histórico gerado anteriormente.
    gerar_xlsx(carteira, historico_carteira)
