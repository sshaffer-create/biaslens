import streamlit as st
import qrcode
from PIL import Image

st.title("QR Code Generator")

data = st.text_input("Enter text or URL", "Python is fun")
img = qrcode.make(data)
img.save("MyQRCode1.jpg")
img = Image.open("MyQRCode1.jpg")

st.image(img)




