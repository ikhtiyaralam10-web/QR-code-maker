#this is the library for generating qr code
import qrcode

link = input("Enter the link: ").strip()
file_path ="C:\\Users\\ikhti\\OneDrive\\Desktop\\qr code\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(link)

img = qr.make_image()
img.save(file_path)

