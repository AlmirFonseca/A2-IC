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
    "AMZN":{
        "ticker": "AMZN",
        "quantidade": 10,
        "tipo": "Ação",
        "nome": "Amazon.com, Inc.", 
        "valor_unitario": 1254,
        "valor_total": 12540
    }, 
    "STNE":{
        "ticker": "STNE",
        "quantidade": 20,
        "tipo": "Ação",
        "nome": "StoneCo Ltd.", 
        "valor_unitario": 1254,
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
    "STNE":{
        "ticker": "AMZN",
        "quantidade": 10,
        "tipo": "Ação",
    },
    "AMZN":{
        "ticker": "STNE",
        "quantidade": 20,
        "tipo": "Ação",
    },
}


def nova_carteira(carteira):
    #listando as chaves do dicionario
    lista_tickers = list(carteira.keys())
    
    #contando o número chaves
    numero_tickers = len(carteira.keys())
    
    #transformando a lista de chaves em string
    string_nomes = " ".join(lista_tickers)

    #utilizando o nome das chaves como Ticker de cada ativo
    info_tickers = Ticker(string_nomes)

    #utilizando os nomes dos ativos como Tickers para acessar as informações
    dict_tickers_dados = info_tickers.price

    #looping para acessar os dados necessários através dos dicionário e atualizando o modelo para ser utilizado no próximo passo do projeto
    for ticker in lista_tickers:
        try:
            nome_ticker = dict_tickers_dados[ticker]['shortName'] #KeyError nessa linha quando a chave estiver vazia! #TypeError para nome inválido!
        except KeyError:
            del carteira[ticker] #destruir parte do dicionário afetada
            continue
        except TypeError:
            del carteira[ticker] #destruir parte do dicionário afetada
            continue
        else:
            #caso não ocorra erros será executado normalmente
            nome_ticker = dict_tickers_dados[ticker]['shortName']
            valor_atualizado = dict_tickers_dados[ticker]['regularMarketPrice']
            valor_total = valor_atualizado * carteira[ticker]["quantidade"]
            dict_novo_dados = {"nome": nome_ticker, "valor_unitario": valor_atualizado, "valor_total": valor_total}
            carteira[ticker].update(dict_novo_dados)
    #verificação da carteira caso ela seja vazia
    if carteira == {}:
        return("Alerta de dicionario vazio!")
    else:
        #atualizando a lista de chaves do dicionario
        lista_tickers = list(carteira.keys())
        
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
        
        #retornando a carteira e o histórico de dados
        return carteira, dados_historico

print(nova_carteira(carteira_modelo))