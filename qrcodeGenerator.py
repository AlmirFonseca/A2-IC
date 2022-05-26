import qrcode

def gerar_qrcode(valor_carteira):
    qr_content = "O valor total da sua carteira é: R$" + str(valor_carteira)
    qr_filename = "QRCode.png"
    qr_object = qrcode.make(qr_content)
    qr_img = qr_object.save(qr_filename)

    return qr_filename