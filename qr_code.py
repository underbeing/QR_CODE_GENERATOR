import qrcode as qr

img = qr.make("www.google.com")
img.save("google.jpg")