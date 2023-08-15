"""
Check whether the entered year is leap year or not.
"""

year = int(input("Enter the year : "))

check_1 = year % 4

if (year % 4) != 0 :
    print("Not a leap year")
elif (year % 100) != 0 :
    print("Leap year")
elif (year % 400) != 0:
    print("Not a Leap year")
else : 
    print("Leap year")