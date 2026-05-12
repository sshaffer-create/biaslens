bill= float(input("Enter the bill amount: "))
tip_percent = float(input("Enter the tip percentage (e.g., 10, 15, 18): "))

tip_amount = bill * (tip_percent/ 100)
total_amount = bill+tip_amount

print("Your total bill, including tip is:", total_amount)
round(total_amount,2)




temperature = float(input("Enter the temperature value: "))
unit = input("Is this in C or F? ")

unit = unit.upper()

if unit == "C":
    converted = (temperature * 9/5)+32
    print("Temperature in Fahrenheit is", round(converted, 2))

elif unit == "F":
    converted = (temperature -32)*(5/9)
    print("Temperature in Celsius is", round(converted, 2))

else:
    print("Invalid input. Please type C or F.")
