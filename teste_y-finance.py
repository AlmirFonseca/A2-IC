from ast import Continue, Pass
import yfinance as yf
import pandas as pd
from yahooquery import Ticker

#Pequena simulação de preenchimento de dicionário partir dos dados recebidos do scrapping.

#Pequena simulação de consulta de valores através de dict

#necessário tratamento de exceções e falhas: ticker inexistente, dict vazio.

#função info sem yahooquery é inviável!

#ticker é importantíssimo!

#função para encontrar o current price da ação <regularMarketPrice>

#carteira_modelo final

#alterar o modelo do código para funções

#histórico das ações: 1 ano de período, e 1 dia de intervalo, entregar valor de fechamento em um df separado

#arquivo.txt "requirements" para a instalação das bibliotecas por pip install -requirements


'''
carteira_modelo = {
    AMZN:{
        "ticker": "AMZN",
        "quantidade": 10,
        "tipo": "Ação",
        "nome": "Amazon.com, Inc.", 
        "valor_unitário": 1254,
        "valor_total": 12540
    }, 
    STNE:{
        "ticker": "STNE",
        "quantidade": 20,
        "tipo": "Ação",
        "nome": "StoneCo Ltd.", 
        "valor_unitário": 1254,
        "valor_total": 25080,
    },      
}
'''

#carteira_modelo inicial
carteira_modelo = {
    "  ":{
        "ticker": "AMZN",
        "quantidade": 10,
        "tipo": "Ação",
    }, 
    "asdfakjsdkfkajsdf":{
        "ticker": "STNE",
        "quantidade": 20,
        "tipo": "Ação",
    },
    "AMZN":{
        "ticker": "AMZN",
        "quantidade": 10,
        "tipo": "Ação",
    },
    " ":{
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
    try:
        nome_ticker = dict_tickers_dados[ticker]['shortName'] #KeyError nessa linha quando a chave estiver vazia! #TypeError para nome inválido!
    except KeyError:
        print("Chave vazia!")
        del carteira_modelo[ticker]
        #destruir parte do dicionário afetada
        Continue
    except TypeError:
        print("Nome inválido!")
        del carteira_modelo[ticker]
        #destruir parte do dicionário afetada
        Continue
    else:
        nome_ticker = dict_tickers_dados[ticker]['shortName']
        valor_atualizado = dict_tickers_dados[ticker]['regularMarketPrice']
        valor_total = valor_atualizado * carteira_modelo[ticker]["quantidade"]
        dict_novo_dados = {"nome": nome_ticker, "valor_unitario": valor_atualizado, "valor_total": valor_total}
        carteira_modelo[ticker].update(dict_novo_dados)
        print("ok")

print(carteira_modelo)

#resgatando os dados na forma de um dataframe de cada ticker

if carteira_modelo == {}:
    print("dicionario vazio")
else:
    dados_historico = yf.download(list(carteira_modelo.keys()), period = "1y", interval="1d")
    print(dados_historico.columns)
    print(dados_historico)