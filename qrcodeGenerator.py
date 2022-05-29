import qrcode

# Função responsável por gerar um QR Code contendo o valor total da carteira
def gerar_qrcode(valor_carteira):
    # Gera uma string com o valor da carteira, mas com o padrão de pontuação americano
    string_valor_carteira = "{:,.2f}".format(round(valor_carteira, 2))

    # Altera as "," por ".", e vice-versa, alterando a string para o padrão brasileiro
    lista_auxiliar = list(string_valor_carteira)
    for index, character in enumerate(lista_auxiliar):
        if character == ",":
            lista_auxiliar[index] = "."
        elif character == ".":
            lista_auxiliar[index] = ","
    string_valor_carteira = "".join(lista_auxiliar)

    # Concatena o valor da carteira à uma frase, montando o conteúdo do qr code
    qr_content = "O valor total da sua carteira é: R$ " + str(string_valor_carteira)
    # Define o nome do arquivo a ser gerado
    qr_filename = "QRCode.png"

    # Cria um imagem com o qrcode e insere nele o conteúdo presente em "qr_content"
    img = qrcode.make(qr_content)
    # Salva a imagem
    img.save(qr_filename)

    # Retorna o nome do arquivo, que é o caminho relativo até ele
    return qr_filename