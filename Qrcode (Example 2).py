#this code allows us to create a simple colored qr code
#that shows a sentence, wifipassword or youtube video
import qrcode
from PIL import Image #this line allow us to work with function called Image (used below)
data = "https://www.youtube.com/watch?v=MFEhbfe7-jk&ab_channel=NimsDai" #or put some text
qr = qrcode.QRCode(version = 1,
            box_size = 10,
            border = 5)
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill_color = 'red',
               back_color = 'white')
img.save('MyQRCode2.png')
img = Image.open("MyQRCode2.png") #this will open the qrcode we created in line above
img.show()  #this will show us the qrcode