#We are creating a Qrcode that has tranparent image as overlay
#on it
# Import Files & Libraries #
import qrcode
from PIL import Image

# Logo Variables For Transparency #
img = Image.open('csumb.jpg') # Allows us to open CSUMB logo image #
img1 = img.convert("RGBA") # Converts image to an RGBA format #

img2 = img1.getdata() # Allows to pull RGBA data from the image #

# Logo Transparency #
newData = [] # Variable that will store new RGB data for the image #
for item in img2:
    if item[:3] == (255, 255, 255): # Pulls the white RGB value from the CSUMB logo #
        newData.append((255, 255, 255, 0)) # Then replaces the white with transparency/red RGB value #
    else:
        newData.append(item)
img1.putdata(newData) # Applies changes to the image
img1.save("csumb.png") # Saves the new image with the updated data #

# Logo Variables For QR Insertion #
Logo_Link = 'csumb.png'
Logo = Image.open(Logo_Link)

# Logo Set-Up Coding #

basewidth = 100
wpercent = basewidth/float(Logo.size[0])
hsize = int(Logo.size[1]*float(wpercent))
Logo = Logo.resize((basewidth, hsize), Image.ANTIALIAS)

# QR Code Set-Up Coding #

QRCode = qrcode.QRCode(
    error_correction = qrcode.constants.ERROR_CORRECT_H
    )
URL = 'https://youtu.be/9XLeGxPRINE'
QRCode.add_data(URL)
QRimg = QRCode.make_image(
    fill_color = 'red', back_color = 'white').convert('RGB')

# Print & Save QR Code #

diff = (QRimg.size[0]-Logo.size[0])//2, (QRimg.size[1]-Logo.size[1])//2
QRimg.paste(Logo, diff,Logo)
QRimg.save('TheNewestQRCode.png')
img = Image.open('TheNewestQRCode.png')
img.show()