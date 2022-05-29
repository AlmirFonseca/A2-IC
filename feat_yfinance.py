import yfinance as yf
import pandas as pd
from yahooquery import Ticker

#TODO Pequena simulação de preenchimento de dicionário partir dos dados recebidos do scrapping.

#TODO Pequena simulação de consulta de valores através de dict

def analisar_carteira(carteira):
    #listando as chaves do dicionario
    lista_tickers = list(carteira.keys())

    #transformando a lista de chaves em string
    string_tickers = " ".join(lista_tickers)

    #utilizando o nome das chaves como Ticker de cada ativo
    info_tickers = Ticker(string_tickers)

    #utilizando os nomes dos ativos como Tickers para acessar as informações
    dict_tickers_dados = info_tickers.price

    #looping para acessar os dados necessários através dos dicionário e atualizando o modelo para ser utilizado no próximo passo do projeto
    for ticker in lista_tickers:
        try:
            nome_ticker = dict_tickers_dados[ticker]['shortName'] #KeyError nessa linha quando a chave estiver vazia! #TypeError para nome inválido!
            valor_atualizado = dict_tickers_dados[ticker]['regularMarketPrice']
        except KeyError:
            del carteira[ticker] #deletar parte do dicionário afetada
            continue
        except TypeError:
            del carteira[ticker] #deletar parte do dicionário afetada
            continue
        else:
            #caso não ocorra erros será executado normalmente
            nome_ticker = dict_tickers_dados[ticker]['shortName']
            valor_atualizado = dict_tickers_dados[ticker]['regularMarketPrice']
            valor_total = float(valor_atualizado) * float(carteira[ticker]["quantidade"])
            dict_novo_dados = {"nome": nome_ticker, "valor_unitario": valor_atualizado, "valor_total": valor_total}
            carteira[ticker].update(dict_novo_dados)

def obter_historico_ativos(carteira):
    if carteira == {}:
        return("Carteira vazia!")

    #listando as chaves do dicionario
    lista_tickers = list(carteira.keys())

    #contando o número chaves
    numero_tickers = len(carteira.keys())

    #resgatando os dados na forma de um dataframe de cada ticker
    data_download = yf.download(lista_tickers, period = "1y", interval="1d", progress=False)

    #criando um novo dataframe com on índices do antigo
    dados_historico = pd.DataFrame(index=data_download.index)

    #preenchendo o novo dataframe com as colunas do antigo
    if numero_tickers == 1: #se houver apenas 1 ticker
        for ticker in lista_tickers:
            dados_historico[ticker] = data_download["Close"] #o acesso se dá através de 1 chave
    elif numero_tickers > 1: #se houver mais de 2 tickers
        for ticker in lista_tickers:
            dados_historico[ticker] = data_download["Close"][ticker] #o acesso se dá através de 2 chaves

    return dados_historico

## Testando
#carteira_modelo para testes
# carteira_modelo = {
#     "  ":{
#         "ticker": "AMZN",
#         "quantidade": 10,
#         "tipo": "Ação",
#     },
#     "asdfakjsdkfkajsdf":{
#         "ticker": "STNE",
#         "quantidade": 20,
#         "tipo": "Ação",
#     },
#     " ":{
#         "ticker": "AMZN",
#         "quantidade": 10,
#         "tipo": "Ação",
#     },
#     " asdsadf ":{
#         "ticker": "STNE",
#         "quantidade": 20,
#         "tipo": "Ação",
#     },
# }
#
# analisar_carteira(carteira_modelo)
#
# print(carteira_modelo)
# print(obter_historico_ativos(carteira_modelo))
