import qrcode


data =input("Enter the link :")
img  = qrcode.make(data)
img.save("qr_myimg.png")
