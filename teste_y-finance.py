from tkinter import N
import yfinance as yf
import pandas as pd

#Pequena simulação de preenchimento de dicionário partir de quantidade de tipo de moedas e
#seus nomes.

#Pequena simulação de consulta de valores através de dict

#necessário tratamento de exceções e falhas

#não consegui lidar com as moedas ainda

#ticker de moeda e ticker de ação

carteira = {
    1:{
        "ticker": "AMZN",
        "quantidade": 10,
        "tipo": "ação"
    }, 
    2:{
        "ticker": "STNE",
        "quantidade": 20,
        "tipo": "ação"
    },   
    3:{
        "ticker": "USD/BRL=X",
        "quantidade": 1000,
        "tipo": "moeda"
    }    
}

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
