#the code below allows us to Download
#Instagram Profile Picture of a stranger or a friend:

import instaloader
ig = instaloader.Instaloader()
dp = input("Enter Insta Username: ")
ig.download_profile(dp, profile_pic_only=True)

#IF, elif, and else function
a = 30
b = 200
if b>a:
    print("b is greater than a")

#a loan application:
# if high income give loan.
# or give loan if the person has high creditscore or a gurantor

high_income = False
has_guarantor = True
has_high_creditscore = False

if high_income:
    print("Eligible for loan because of high income")
elif has_guarantor or has_high_creditscore:
    print("Eligible for loan because of gurantor or creditscore")
else:
    print("Not eligible for loan")


#Weight Conversion app.
#1 lbs is 0.45 kg.

weight = input("What is your weight?")
unit = input("Was the weight you typed above in lbs or kgs?")
if unit.lower() == "lbs":  #if unit.upper() =="LBS"
    ConvertedWeight = float(weight)*0.45
    print("Your weight in Kgs " + str(ConvertedWeight))

else:
    ConvertedWeight = float(weight) / 0.45
    print("Your weight in lbs " + str(ConvertedWeight))

    #SAT Score
    # if someone's SAT score is 500 and less, we give a statement called your score is low
    #if 501 to 1200, your score is okay
    # if 1201 and above, your score is good

    name = input("What is your name?")
    score = input("What is your SAT score?")

    if int(score)<0 or int(score)>1600:
        print ("Invalid SAT score")
    elif int(score)<=500:
        print(name +" your score is low")
    elif int(score)<=1200: #elif score>=501 and score <=1200
        print(name + " your score is okay")
    else:
        print(name + " your score is good")

#We are now learning about library
#we are creating a QR code
#Install two libraries PILlow and QR Code

import qrcode
from PIL import Image
data = ("https://www.youtube.com/watch?v=Oxf8ULSB8yU&list=RDOxf8ULSB8yU&start_radio=1")
apple = qrcode.make(data)
apple.save("MyQrCode.jpg") #SAVE it as image file
apple.show()  #Can you open the file?
