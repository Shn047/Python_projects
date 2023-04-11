import qrcode

qr = qrcode.QRCode(
    version= 15,
    box_size= 10,
    border= 5
)

data = input("Enter URL link which you want to generate QR Code : ")

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

split_list = data.split('.')
name = split_list[1]
img.save(name+"_QRcode.png")