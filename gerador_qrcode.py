import qrcode

# Função "gerar_qrcode" -> responsável por gerar o qrcode a partir do input "valor_carteira" e retornar o caminho relativo da imagem salva
def gerar_qrcode(valor_carteira):
    # A string "qr_content" concatena uma frase ao valor total da carteira
    qr_content = "O valor total da sua carteira é: R$" + str(valor_carteira)
    # A string "qr_filename" armazena o caminho até a imagem a ser criada
    qr_filename = "QRCode.png"

    # É inicializado o objeto que constrói o qrcode
    qr_img = qrcode.make(qr_content)
    # A imagem é salva
    qr_img.save(qr_filename)

    # A função retorna o caminho relativo da imagem gerada
    return qr_filename