from tkinter import N
import yfinance as yf
import pandas as pd

#Pequena simulação de preenchimento de dicionário partir de quantidade de tipo de moedas e
#seus nomes.

#Pequena simulação de consulta de valores através de dict

#necessário tratamento de exceções e falhas

#não consegui lidar com as moedas ainda


quantidade_moeda = int(input("Quantidade de moedas: "))
dict_data = {'moeda': [], 'ticker': []}
contador = 0

while contador < quantidade_moeda:
    tipo_moeda = input("Insira o tipo da moeda: ")
    dict_data['moeda'].append(tipo_moeda)
    contador+=1

contador = 0

quantidade_ticker = int(input("Quantidade de tickers: "))
while contador < quantidade_ticker:
    tipo_ticker = input("Insira o tipo de ticker: ")
    dict_data['ticker'].append(tipo_ticker)
    contador+=1

contador = 0

print(dict_data)

while contador < quantidade_ticker:
    ticker = yf.Ticker(dict_data['ticker'][contador])
    ticker_historical = ticker.history(start="2022-05-05", end="2022-06-05", interval="1d")
    print(ticker_historical)
    contador+=1

contador = 0


#possível código para moedas

while contador < quantidade_moeda:
    ticker = yf.Ticker(dict_data['moeda'][contador])
    ticker_historical = ticker.history(start="2022-05-05", end="2022-06-05", interval="1d")
    print(ticker_historical)
    contador+=1
