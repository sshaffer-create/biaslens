import qrcode
from PIL import Image #this line allow us to work with function called Image from PILlow library, which we have used below)
data = 'Python is fun'  # or put a youtube link instead of words
img = qrcode.make(data)
img.save('MyQRCode1.jpg')
img = Image.open("MyQRCode1.jpg") #this will open the qrcode we created in line above. Image.open() is the Image module from PIL library that allows us to open the image file named isntide ().
img.show()  #this will show us the qrcode


import streamlit as st
import qrcode
from PIL import Image  # allows us to use Image functions from Pillow library

# Optional improvement (not required):
# st.title("QR Code Generator")

data = st.text_input("Enter text or URL", "Python is fun")  # creates an input box; default text is "Python is fun"
img = qrcode.make(data)  # generate QR code from whatever user enters
img.save('MyQRCode1.jpg')  # save QR code as image file
img = Image.open("MyQRCode1.jpg") # open the saved QR code image
st.image(img) # display the QR code in the Streamlit web app

"""
#in the code above if you want a button to generate the QR code, you change it to following code (line 17 remains same)
data = st.text_input("Enter text or URL", "Python is fun")
if st.button("Generate QR Code"):
    img = qrcode.make(data)
    img.save('MyQRCode1.jpg')
    img = Image.open("MyQRCode1.jpg")
    st.image(img)
"""


