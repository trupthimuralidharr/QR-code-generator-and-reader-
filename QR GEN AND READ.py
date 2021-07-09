import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("HI GUYSSS!!!")
qr.png("code.png",scale=8)

d= decode(Image.open("code.png"))
print(d[0].data.decode("ascii"))