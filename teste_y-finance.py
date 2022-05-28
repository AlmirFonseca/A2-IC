import yfinance as yf
import pandas as pd
from yahooquery import Ticker

#Pequena simulação de preenchimento de dicionário partir dos dados recebidos do scrapping.

#Pequena simulação de consulta de valores através de dict

#necessário tratamento de exceções e falhas

#função info sem yahooquery é inviável!

#ticker é importantíssimo!

#função para encontrar o current price da ação <regularMarketPrice>

#carteira_modelo final

#histórico das ações: 1 ano de período, e 1 dia de intervalo, entregar valor de fechamento em um df separado

#arquivo.txt "requirements" para a instalação das bibliotecas por pip install -requirements


'''
carteira_modelo = {
    AMZN:{
        "ticker": "AMZN",
        "quantidade": 10,
        "tipo": "Ação",
        "nome": "Amazon.com, Inc.", ---> desistir por agora
        "valor_unitário": 1254,
        "valor_total": 12540
    }, 
    STNE:{
        "ticker": "STNE",
        "quantidade": 20,
        "tipo": "Ação",
        "nome": "StoneCo Ltd.", ---> desistir por agora
        "valor_unitário": 1254,
        "valor_total": 25080,
    },      
}
'''

#carteira_modelo inicial
carteira_modelo = {
    "AMZN":{
        "ticker": "AMZN",
        "quantidade": 10,
        "tipo": "Ação",
    }, 
    "STNE":{
        "ticker": "STNE",
        "quantidade": 20,
        "tipo": "Ação",
    },      
}

#lista das chaves do dicionário modelo
lista_nomes = list(carteira_modelo.keys())

#transformando a lista em string
string_nomes = ' '.join(lista_nomes)

#utilizando o nome das chaves como Ticker de cada ativo
info_tickers = Ticker(string_nomes)

#utilizando os nomes dos ativos como Tickers para acessar as informações
dict_tickers_dados = info_tickers.price

#looping para acessar os dados necessários através dos dicionário e atualizando o modelo para ser utilizado no próximo passo do projeto
for ticker in lista_nomes:
    nome_ticker = dict_tickers_dados[ticker]['shortName']
    valor_atualizado = dict_tickers_dados[ticker]['regularMarketPrice']
    valor_total = valor_atualizado * carteira_modelo[ticker]["quantidade"]
    dict_novo_dados = {"nome": nome_ticker, "valor_unitario": valor_atualizado, "valor_total": valor_total}
    carteira_modelo[ticker].update(dict_novo_dados)

print(carteira_modelo)

#resgatando os dados na forma de um dataframe de cada ticker
dados_historico = yf.download(lista_nomes, period = "1y", interval="1d")
dados_historico = dados_historico["Close"]

print(dados_historico.columns)
print(dados_historico)