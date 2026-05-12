#creating RockPaperScissors Gam
#Rules: Rock>scissors; Paper >rock.Scissors > paper.

import random
user_action = input('Enter a choice of rock, paper, or scissors: ')
possible_action = ['rock', 'paper', 'scissors']
computer_action = random.choice(possible_action)
print('You chose ' + user_action + '. Computer chose ' + computer_action + '.')

if user_action.lower() ==computer_action:
    print('Both players selected ' + user_action + '. It is a tie.')
elif user_action.lower() == 'rock':
    if computer_action == 'scissors':
        print('Rock smashes scissors. You win.')
    else:
        print('Paper covers rock. You lose.')

elif user_action.lower() == 'scissors':
    if computer_action == 'paper':
        print('Scissors cuts the papers. You win')
    else:
        print('Rock smashes scissors. You lose')

elif user_action.lower() == 'paper':
    if computer_action == 'rock':
        print('Paper covers the rock. You win')
    else:
        print('Scissors cut paper. You lose')


#make QR code yellow
import qrcode
from PIL import Image
data = ("https://www.youtube.com/watch?v=Oxf8ULSB8yU&list=RDOxf8ULSB8yU&start_radio=1")
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(data)
qr.make(fit=True)

apple = qr.make_image(
    fill_color="red",
    back_color="white"
)

apple.save("secondQR.jpg")
apple = Image.open("secondQR.jpg")
apple.show()


