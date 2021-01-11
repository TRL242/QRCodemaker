import qrcode
#from PIL import Image, ImageDraw
from image import *

import qrcode.image.base

#Simple QRCode
img = qrcode.make("Test Image.")
img.save("mycode.png")

# #QRCODE to website link
# qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20,border=2)
#
# qr.add_data("harboursidedentistry.com")
# qr.make(fit=True)
#
# img = qr.make_image(fill_color="black", back_color="white")
# img.save("HSDentistry.png")