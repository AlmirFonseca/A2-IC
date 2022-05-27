from tkinter import N
import yfinance as yf
import pandas as pd

#Pequena simulação de preenchimento de dicionário partir de quantidade de tipo de moedas e
#seus nomes.

#Pequena simulação de consulta de valores através de dict

#necessário tratamento de exceções e falhas

#não consegui lidar com as moedas ainda

#ticker de moeda e ticker de ação

#função para encontrar o current price da ação <regularMarketPrice>

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




'''
while contador < quantidade_moeda:
    tipo_moeda = input("Insira o ticker das moedas: ")
    dict_dado['moeda'].append(tipo_moeda)
    contador+=1

contador = 0

quantidade_ticker = int(input("Quantidade de tipos de ação: "))
while contador < quantidade_ticker:
    tipo_ticker = input("Insira o ticker das ações: ")
    dict_dado['ticker'].append(tipo_ticker)
    contador+=1

contador = 0

print(dict_dado)

while contador < quantidade_ticker:
    ticker = yf.Ticker(dict_dado['ticker'][contador])
    ticker_historical = ticker.history(start="2022-05-05", end="2022-06-05", interval="1d")
    print(ticker_historical)
    contador+=1

contador = 0

#possível código para moedas

while contador < quantidade_moeda:
    ticker = yf.Ticker(dict_dado['moeda'][contador])
    ticker_historical = ticker.history(start="2022-05-05", end="2022-06-05", interval="1d")
    print(ticker_historical)
    contador+=1

'''
