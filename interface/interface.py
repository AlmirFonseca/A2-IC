import validators

# Função que recebe entrada de url e checa a sua validez
def entrada_url():
    # Inicializa uma variável sentinela, que irá controlar a repetição abaixo
    url_valida = False
    # Enquanto não houver uma entrada de URL válida, o bloco abaixo se repete
    while url_valida != True:
        # Aguarda a inserção de uma URL com a carteira de ativos a ser analisada
        url_entrada = str(input('Insira o URL da carteira de investimentos a ser analisada: \n'))
        
        # Caso nenhum valor seja inserido
        if url_entrada == "":
            print("\nNenhuma URL foi inserida. Por favor, tente novamente")
            continue
        
        # Checa se a URL é válida
        url_valida = validators.url(url_entrada)
        
        # Se a URL for válida, a função a retorna
        if url_valida == True:
            print("\nAguarde. Estamos analisando sua carteira...\n")
            return url_entrada
        else:
            print("\nURL inválida! Por favor, tente novamente")