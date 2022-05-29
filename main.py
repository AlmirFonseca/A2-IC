from scrapping import constroi_objeto_carteira
from feat_yfinance import analisar_carteira, obter_historico_ativos
from openpyxl_generator import gerar_xlsx

# Função para construir a carteira e retorna dicioário com papéis e quantidades a partir de link do site.
carteira = constroi_objeto_carteira("https://marianalima2000.github.io/A2-IC/carteira.html")

# Funções que tratam os valores e constroem o histórico dos ativos a partir da lib yfinance
analisar_carteira(carteira)
historico_carteira = obter_historico_ativos(carteira)

#Função que gera os resultados a partir da carteira atual e do histórico gerado anteriormente.
gerar_xlsx(carteira, historico_carteira)
