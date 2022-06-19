# A2-IC
Repositório do trabalho de Introdução a Computação (A2-2022.1), projeto com o objetivo de **ler uma carteira em .html utilizando python e gerar uma análise dos seus dados**.

## Como usar:
1. Rode o comando ```pip install -r requirements.txt``` para baixar todas as dependências necessárias.
2. Rode o programa utilizando o comando ```python main.py``` para rodar o arquivo inicial do repositório. Na sequência, siga as instruções, inserindo a URL da carteira a ser analisada.

## Carteiras base utilizadas:
- https://almirfonseca.github.io/A2-IC/carteira_abner.html
- https://almirfonseca.github.io/A2-IC/carteira_almir.html
- https://almirfonseca.github.io/A2-IC/carteira_mariana.html

## Resultados:
O resultado da função consiste em um arquivo ".xlsx" a ser encontrado na pasta "Resultados" após a conclusão da análise.

Dentro do arquivo gerado há 5 abas:
1. Primeira aba contendo uma tabela, a qual resume a situação atual da carteira (seus ativos, quantidades e preços atuais) 
2. Segunda aba contendo o primeiro gráfico, que exibe o Share da carteira (percentual de cada ativo presente na carteira). 
3. Terceira aba contendo o segundo gráfico, que exibe a variação relativa de todos os ativos presentes na carteira no último ano. 
4. Quarta aba contendo o terceiro gráfico, que exibe a variação do valor total da carteira ao longo no último ano. 
5. Quinta e última aba contendo o QR Code que, ao ser lido, informa o valor atual da carteira.