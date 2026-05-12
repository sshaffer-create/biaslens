veg =["apple", "banana", "orange"]
for x in veg:
    print(x)

veg = [90, 99, 100]
for x in veg:
    print(x)

shopping_prices = [10, 20, 30]
total = 0
for item in shopping_prices:
    total = total + item #or it can be written as total += item
print('Tpotal Shopping Cost: ', total)

#while loop practice
apple = 2
while apple<= 5:
    print(apple)
    apple = apple + 1

Password = "admin123"
guess_count = 0
guess_limit = 4

while guess_count < guess_limit:
    guess = input("Input your password: ")
    if guess == Password:
        print("Your Password is correct!You can continue your work")     # when the trial is correct, this is printed
        break     # Allows us to break the while loop
    else:
        guess_count = guess_count + 1  # Equivalent to guess_count = guess_count + 1
        attempts_left = guess_limit - guess_count

        if guess_count >0:
            #print(f" Incorrect password. {attempts_left} attempt(s) remaining."
            print("Incorrect password", attempts_left, "attempts remaining")
        else:
            print("Sorry, too many failed attempts")  # this is printed after three attempts


