#this code allows us to create a simple black and white qr code
#that shows a sentence, wifipassword or youtube video
import qrcode
from PIL import Image #this line allow us to work with function called Image (used below)
data = 'Python is fun'  # or put a youtube link instead of words
img = qrcode.make(data)
img.save('MyQRCode1.jpg')
img = Image.open("MyQRCode1.jpg") #this will open the qrcode we created in line above
img.show()  #this will show us the qrcode