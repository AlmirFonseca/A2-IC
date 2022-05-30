import requests
from bs4 import BeautifulSoup

# Função recebendo url da página a ser mapeada e respondendo o soup dela
def get_carteira_from_url(url):
    # Fazendo request para obter o response da págima
    response = requests.get(url)
    # Utilizando p BeatifulSoup para ter o conteúdo do html de mais fácil manejo
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

# Função que recebe soup já parseado e retorna carteira formatada de moedas
def moedas_from_soap(soup):
    # Pega todos os objetos do html dentro da class moeda
    moedas = soup.find(class_="moeda")
    # pega todos os itens do html destacado que tem a tag td
    itens = moedas.find_all("td")
    carteira_moedas = {}
    # passa por todos os objetos de tag td, aqui contendo os nomes das moedas e valor delas
    for i in range(len(itens)):
        # Testa para ver se o índice do objeto em itens é par, para apenas pegarmos aqui o nome da moeda.
        if i%2 == 0:
            nome_moeda = itens[i].string
            # adiciona o itwm i + 1 por ser o valor da moeda que pegamos no teste para ver se é par.
            quantidade_moeda = float(itens[i+1].string) if itens[i+1].string else None
            # formata no padrão desejado e adiciona no dict de todas as moedas.
            moeda = {
                "ticker": nome_moeda,
                "quantidade": quantidade_moeda,
                "tipo": "Moeda"
            }
            carteira_moedas[nome_moeda]=moeda
    return carteira_moedas

# Função que recebe soup já parseado e retorna carteira formatada de ações
## Utilização e comentários idênticos ao anterior apenas utilizando ações ao invés de moedas.
def acoes_from_soap(soup):
    acoes = soup.find(class_="acao")
    itens = acoes.find_all("td")
    carteira_acoes = {}
    for i in range(len(itens)):
        if i%2 == 0:
            nome_acao = itens[i].string
            quantidade_acao = float(itens[i+1].string) if itens[i+1].string else None
            acao = {
                "ticker": nome_acao,
                "quantidade": quantidade_acao,
                "tipo": "Ação"
            }
            carteira_acoes[nome_acao]=acao
    return carteira_acoes

# Função que retorna carteira final no formato desejado juntando as carteiras de acoes e moedas utilizando as funções anteriores.
def constroi_objeto_carteira(url):
    # Função que retorna soup formatado
    soup = get_carteira_from_url(url)
    # Função que retorna carteira de moedas (dict)
    moedas = moedas_from_soap(soup)
    # Função que retorna carteira de acoes (dict)
    acoes = acoes_from_soap(soup)
    # método para juntar 2 dicionários, obtendo 1 dict apenas no fim.
    carteira = {**acoes, **moedas}
    return carteira


### Testando:
# carteira = constroi_objeto_carteira("https://marianalima2000.github.io/A2-IC/carteira.html")
# print(carteira)
