import yfinance as yf
import pandas as pd
from yahooquery import Ticker

def analisar_carteira(carteira):
    #listando as chaves do dicionario
    lista_tickers = list(carteira.keys())

    #transformando a lista de chaves em string
    string_tickers = " ".join(lista_tickers)

    #utilizando o nome das chaves como Ticker de cada ativo
    info_tickers = Ticker(string_tickers)

    #utilizando os nomes dos ativos como Tickers para acessar as informações
    dict_tickers_dados = info_tickers.price
    
    tipos_moedas_estrangeiras = {}

    #looping para acessar os dados necessários através dos dicionário e atualizando o modelo para ser utilizado no próximo passo do projeto
    for ticker in lista_tickers:
        try:
            #acessa os valores relativos ao ticker(ativo)
            info_ticker_ativo = dict_tickers_dados[ticker]
            
            #busca, dentro dos resultados do ativo, valores como nome, valor atual e moeda em que o ativo é exibido
            nome_ticker = info_ticker_ativo['shortName'] #KeyError nessa linha quando a chave estiver vazia! #TypeError para nome inválido!
            valor_atualizado = info_ticker_ativo['regularMarketPrice']
            unidade_moeda = info_ticker_ativo['currency']
        except KeyError:
            del carteira[ticker] #deletar parte do dicionário afetada
            continue
        except TypeError:
            del carteira[ticker] #deletar parte do dicionário afetada
            continue
        else:
            #caso não ocorra erros será executado normalmente
            
            #retirando os espaços em branco a mais de certos nomes, como o de PETR4.SA ("PETROBRAS   PN  EDJ N2")
            nome_ticker = " ".join(nome_ticker.split())
            
            #adicionar a um dicionario a moeda em que o ativo é exibido, junto do ticker relacionado à sua cotação em Reais (BRL)
            tipos_moedas_estrangeiras[unidade_moeda] = {"ticker_conversao_BRL": unidade_moeda.upper()+"BRL=X"}
            
            #calcular o valor total investido naquele ativo, na moeda padrão
            valor_total = float(valor_atualizado) * float(carteira[ticker]["quantidade"])
            #atualizar a carteira com os dados coletados a partir do yfinance
            dict_novo_dados = {"nome": nome_ticker, "valor_unitario": valor_atualizado, "valor_total": valor_total, "unidade_moeda": unidade_moeda}
            carteira[ticker].update(dict_novo_dados)
    
    # Remove a moeda BRL do dicionario, pois não queremos converter BRL para BRL
    del tipos_moedas_estrangeiras["BRL"]
    
    # Retorna o dicionario que contém as moedas diferentes de BRL, com os seus tickers de valor em BRL e suas cotações atuais
    return carteira, tipos_moedas_estrangeiras

def obter_historico_ativos(carteira):

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

def converter_valores_BRL(carteira, historico, tipos_moedas_estrangeiras):
    
    # Inicializa uma lista que deve armazenar os tickers que nos permitem obter o valor atual de cada moeda em BRL
    lista_tickers_moedas = []
    
    # Itera as moedas em que as ações são exibidas
    for moeda in tipos_moedas_estrangeiras.values():
        # Popula a lista criada com os tickers de conversão para BRL
        lista_tickers_moedas.append(moeda.get("ticker_conversao_BRL"))

    # Concatena os tickers numa string, separados por " "
    string_moedas = " ".join(lista_tickers_moedas)

    # Cria um Ticker que busca dados a partir dos tickers no Yahoo Finance
    info_moedas = Ticker(string_moedas)
    dict_dados_moedas = info_moedas.price
    
    # Itera as moedas
    for nome_moeda, moeda in tipos_moedas_estrangeiras.items():
        try:
            # Armazena o ticker de conversão para BRL dessa moeda
            ticker_conversao_BRL = moeda.get("ticker_conversao_BRL")
            # Acessa os dados da moeda dentre os resultados da busca através do Yahoo Finance
            info_ticker_moeda = dict_dados_moedas[ticker_conversao_BRL]
            
            # Obtém a cotação atual da moeda em BRL
            valor_conversao_moeda = info_ticker_moeda['regularMarketPrice']
        except KeyError:
            del tipos_moedas_estrangeiras[nome_moeda] #deletar parte do dicionário afetada
            continue
        except TypeError:
            del tipos_moedas_estrangeiras[nome_moeda] #deletar parte do dicionário afetada
            continue
        else:
            # Insere o valor de conversão no dicionario de cada moeda
            moeda["fator_conversao_BRL"] = valor_conversao_moeda
            
    # Conversão dos valores da carteira
    ###########################################################################
    
    # Itera os ativos da carteira para converter os seus valores para BRL
    for ativo in carteira.values():
        # Recebe a moeda em que cada ativo é exibido
        unidade_moeda_ativo = ativo.get("unidade_moeda")
        
        # Caso o ativo seja exibido em BRL, analisamos o próximo, já que não querermos converter BRL em BRL
        if(unidade_moeda_ativo == "BRL"):
            continue
        
        # Recebe os dados sobre a moeda em que o ativo é exibido
        moeda_ativo = tipos_moedas_estrangeiras.get(unidade_moeda_ativo)
        # Recebe a cotação, em BRL, da moeda em que o ativo é exibido
        cotacao_para_BRL = moeda_ativo.get("fator_conversao_BRL")
        
        # Converte determinados valores para BRL, multiplicando-os pelo valor de cada moeda em BRL
        ativo["valor_unitario"] = ativo.get("valor_unitario") * cotacao_para_BRL
        ativo["valor_total"] = ativo.get("valor_total") * cotacao_para_BRL

    # Conversão dos valores da historico de valores
    ###########################################################################
    
    # Resgata as cotações (em BRL) de cada moeda na forma de um dataframe
    cotacoes_download = yf.download(string_moedas, start=historico.index[0], stop=historico.index[-1], interval="1d", progress=False)
    
    #criando um novo dataframe com on índices do antigo para reorganizar as colunas
    historico_cotacoes = pd.DataFrame(index=cotacoes_download.index)
    
    numero_tickers_moedas = len(lista_tickers_moedas)

    #preenchendo o novo dataframe com as colunas do antigo
    if numero_tickers_moedas == 1: #se houver apenas 1 ticker
        for ticker in lista_tickers_moedas:
            historico_cotacoes[ticker] = cotacoes_download["Open"] #o acesso se dá através de 1 chave
    elif numero_tickers_moedas > 1: #se houver mais de 2 tickers
        for ticker in lista_tickers_moedas:
            historico_cotacoes[ticker] = cotacoes_download["Open"][ticker] #o acesso se dá através de 2 chaves
    
    # Itera as colunas/ativos do historico de valores
    for ticker_ativo in historico.columns:
        
        # Acessa os dados na carteira relacionados a esse ticker
        ativo = carteira.get(ticker_ativo)
        # Resgata a moeda em que esses dados estão sendo exibidoos
        unidade_moeda_ativo = ativo.get("unidade_moeda")
        
        # Se os dados do ativo estiverem sendo exibidos em BRL, pulamos para a próxima coluna, pois não há interesse em converter BRL para BRL
        if(unidade_moeda_ativo == "BRL"):
            continue
        # Se os dados estiverem sendo exibidos em outra moeda
        else:
            # Acessa os dados daquela tipo de moeda
            tipo_moeda = tipos_moedas_estrangeiras.get(unidade_moeda_ativo)
            # Obtém o ticker relacionado ao seu valor em BRL
            ticker_conversao_BRL = tipo_moeda.get("ticker_conversao_BRL")
            
            # Multiplica a coluna do historico de valores pela coluna do historico de cotacoes que contém o valor daquela moeda, em BRL, para cada data
            historico[ticker_ativo] *= historico_cotacoes[ticker_conversao_BRL]

# # Testando
# #carteira_modelo para testes
# carteira_modelo = {
#     "  ":{
#         "ticker": "AMZN",
#         "quantidade": 10,
#         "tipo": "Ação",
#     },
#     "Stasdlasn":{
#         "ticker": "STNE",
#         "quantidade": 20,
#         "tipo": "Ação",
#     },
#     "AMZN":{
#         "ticker": "AMZN",
#         "quantidade": 10,
#         "tipo": "Ação",
#     },
#     "STNE":{
#         "ticker": "STNE",
#         "quantidade": 20,
#         "tipo": "Ação",
#     },
#     "USDBRL=X":{
#         "ticker": "USDBRL=X",
#         "quantidade": 20,
#         "tipo": "Moeda",
#     },
#     "GC=F":{
#         "ticker": "GC=F",
#         "quantidade": 20,
#         "tipo": "Moeda",
#     },
#     "AZN.L":{
#         "ticker": "AZN.L",
#         "quantidade": 20,
#         "tipo": "Ação",
#     },
#     "EUR":{
#         "ticker": "EUR",
#         "quantidade": 20,
#         "tipo": "Ação",
#     },
#     "JPY":{
#         "ticker": "JPY",
#         "quantidade": 20,
#         "tipo": "Ação",
#     },
#     "PETR4.SA":{
#         "ticker": "PETR4.SA",
#         "quantidade": 20,
#         "tipo": "Ação",
#     },
#     "CNYBRL=X":{
#         "ticker": "CNYBRL=X",
#         "quantidade": 20,
#         "tipo": "Ação",
#     },
#     "NUBR33.SA":{
#         "ticker": "NUBR33.SA",
#         "quantidade": 20,
#         "tipo": "Ação",
#     },
#     "INR":{
#         "ticker": "INR",
#         "quantidade": 20,
#         "tipo": "Ação",
#     }
# }

# carteira, tipos_moedas = analisar_carteira(carteira_modelo)

# historico_valores = obter_historico_ativos(carteira_modelo)

# converter_valores_BRL(carteira_modelo, historico_valores, tipos_moedas)

# print(carteira_modelo)
# print(historico_valores)

# """with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(obter_historico_ativos(carteira_modelo))"""
