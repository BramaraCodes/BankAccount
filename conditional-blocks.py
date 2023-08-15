# Conditional blocks
# if/else statements
# nested if/else statemets
# elif statements for multiple conditions to execute.

print("Welcome to the roller coaster ride")
height = int(input("Enter your height to enjoy the rollercoaster ride : "))

if height >= 120 :
    print("Heyyy, You're eligible to ride the rollercoaster...!!!!")
    age = int(input("Enter your age to get the absolute entry for the ride : "))
    if age < 12:
        print("Please pay the amount 5$.")
    elif age <= 18 :
        print("Please pay the amount 7$.")
    elif age == 22:
        print("Please pay the amount 10$.")
    else :
        print("Please pay the amount 12$.")
else :
    print("Sorry, honey you're not...!")