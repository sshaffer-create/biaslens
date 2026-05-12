#I am creating a QRCode with a logo of my company
#QRCode, Pillow (also known as PIL)

import qrcode
from PIL import Image

#*****WE ARE WORKING WITH CREATION OF QRCODE*********************
import qrcode
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

url = "https://csumb.edu/"

QRcode.add_data(url)  #now, I added URL variable data to my QRcode I created above.

QRcode.make(fit=True)

#
#QRimg = QRcode.make_image(fill_color= (0, 128, 0),  back_color = "white" ).convert("RGB")
QRimg = QRcode.make_image(fill_color="red", back_color="white")

#*************BELOW WE ARE WORKING ON CSUMB LOGO ***********************
#############################################################################
#I am creating a QRCode with a logo of my company
#QRCode, Pillow (also known as PIL)

import qrcode
from PIL import Image

#*****WE ARE WORKING WITH CREATION OF QRCODE*********************
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

url = "https://csumb.edu/"

QRcode.add_data(url)  #now, I added URL variable data to my QRcode I created above.

QRcode.make(fit=True)

#
#QRimg = QRcode.make_image(fill_color= (0, 128, 0),  back_color = "white" ).convert("RGB")
QRimg = QRcode.make_image(fill_color="red", back_color="white")

#*************BELOW WE ARE WORKING ON CSUMB LOGO ***********************

logo = Image.open("csumb.jpg")

#/* know the 25% size of the QRimg*/

logo_size = QRimg.size[0] // 4

logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

pos = (
    (QRimg.size[0] - logo.size[0])  // 2,
    (QRimg.size[1] - logo.size[1]) // 2
)

QRimg.paste(logo, pos, logo)

QRimg.save("CSUMB_QRCode.png")
QRimg.show()