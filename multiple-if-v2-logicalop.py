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
        print("Child tickets costs 5$.")
    elif age <= 18 :
        bill = 7
        print("Teens tickets costs 7$.")
    elif (age > 45 and age < 55) :
        bill = 0
        print("Tickets for mildlife crisis costs 0$")
    else :
        bill = 10
        print("Adult tickets costs 10$.")

    wants_photos = input("Do you want to take photos along with the ride??...Yes or No. \n")

    if wants_photos == "Yes":
        bill += 3
        print(f"Total bill can costs upto {bill}$ includes taking photos.\n")
    else :
        print(f"Total bill equals to be {bill}$")
else :
    print("Sorry, my little mumschkidde you're out of coaster...!")