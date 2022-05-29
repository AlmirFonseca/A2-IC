from scrapping import constroi_objeto_carteira
from feat_yfinance import analisar_carteira, obter_historico_ativos

# Função para construir a carteira e retorna dicioário com papéis e quantidades a partir de link do site.
carteira = constroi_objeto_carteira("https://marianalima2000.github.io/A2-IC/carteira.html")

# Funções que tratam os valores e constroem o histórico dos ativos a partir da lib yfinance
analisar_carteira(carteira)
historico_carteira = obter_historico_ativos(carteira)

print(historico_carteira)
