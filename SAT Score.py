name = input("What is your name?")
score = input("What is your SAT score?")

if int(score) < 0 or int(score) > 1600:
    print("Invalid SAT score")
elif int(score) <= 500:
    print(name + " your score is low")
elif int(score) <= 1200:  # elif score>=501 and score <=1200
    print(name + " your score is okay")
else:
    print(name + " your score is good")
