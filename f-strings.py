# It returns float number.
print(78/9)

# It returns a float, but with 2-digits of precision after rounding the float.
print(round(78/9, 2))

# Floor division returns the integer.
print(78//9)

# f-Strings
userName = input("enter your username : ")
age = input("enter your age")
if(age == 18) :
 print("You are eligible to play the game")
 print(f"your username and age is {userName} and {age}")
else :
 print("You must be atlest 10 years of age : ")

