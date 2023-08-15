# Multiple if statements
# if/else statements but all the conditions need to be checked and executed.

print("Welcome to the roller coaster ride")
height = int(input("Enter your height to enjoy the rollercoaster ride : "))
bill = 0

if height >= 120 :
    print("Heyyy, You're eligible to ride the rollercoaster...!!!!")
    age = int(input("Enter your age to get the absolute entry for the ride : "))
    if age < 12:
        bill = 5
        print("Please pay the amount 5$.")
        photos = bool(input("Do you want to take pictures along with Ride...!"))
        if photos == "True":
            bill += 3
            print(f"The amount for photos is 3$. Here comes the total amount to be {bill}$")
        else :
            print(f"Thank you, you total bill is {bill}$ only")
    elif age <= 18 :
        bill = 7
        print("Please pay the amount 7$.")
        photos = bool(input("Do you want to take pictures along with Ride...!"))
        if photos == "True":
            bill += 3
            print(f"The amount for photos is 3$. Here comes the total amount to be {bill}$")
        else :
            print(f"Thank you, you total bill is {bill}$ only")
    elif age > 18:
        bill = 10
        print("Please pay the amount 10$.")
        photos = bool(input("Do you want to take pictures along with Ride...!"))
        if photos == "True":
            bill += 3
            print(f"The amount for photos is 3$. Here comes the total amount to be {bill}$")
        else :
            print(f"Thank you, you total bill is {bill}$ only")
else :
    print("Sorry, my little mumschkidde you're out of coaster...!")