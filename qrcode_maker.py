import qrcode
import os
mode = input("1. qrcode con testo\n2. qrcode con link")
if mode == '1':
    text = input('testo -->')
    img = qrcode.make(text)
    img.save("qrcode.png")
    os.system('start qrcode.png')

if mode == '2':
    text = input('url -->')
    qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=20,
                    border=2)

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('urlqr.png')
    os.system('start urlqr.png')