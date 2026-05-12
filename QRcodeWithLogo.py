#create Qrcode with CSUMB logo on it
# We will use an external image file called csumb

import qrcode
from PIL import Image

Logo_Link = "csumb.jpg"
logo = Image.open(Logo_Link)

basewidth = 100 #earlier it was 197

wpercent = basewidth/float(logo.size[0])
hsize = int(logo.size[1]*float(wpercent))

logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

QRcode = qrcode.QRCode(
  error_correction = qrcode.constants.ERROR_CORRECT_H
    )
url = "https://www.youtube.com/watch?v=L7vXZ1BnTBI"

QRcode.add_data(url)

QRimg = QRcode.make_image(
    fill_color = 'green', back_color = 'white').convert('RGB')

diff = (QRimg.size[0]-logo.size[0])//2, (QRimg.size[1]-logo.size[1])//2
QRimg.paste(logo, diff)

QRimg.save("QRnew.png")
img = Image.open("QRNew.png")
img.show()