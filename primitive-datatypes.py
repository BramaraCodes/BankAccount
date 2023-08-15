# Data types : Primitive
# int : integer
num_1 = 123
num_2 = 456
print(num_1*num_2)

#float : Decimals
num_3 = 345.67
num_4 = 346.907
print(num_3*num_4+num_2)

# Bool : Boolean
isLetterMatched = "Bramara"
if(isLetterMatched[0] == "B"):
    print("The is Letter is matched.")
else :
    print("Entered Letter is not matched.")

# Strings : Subscripting -- pulling out individual characters from the strings
user_name = "Bramara"
print("Bramara"[4])
print("123678"[5])
print(user_name[1])

# String manipulations 
# String concatenation
print("123890" + "4678924973")

# Avoid type errors 
# Type Casting helps to convert one data type to suitable data type
char_1 = input("What's is your name?\n")
len_char_1 = str(len(char_1))
print("Your name is " + char_1 + " and it has " + len_char_1 + " characters")

# float numbers
print(70 + float("123.678"))


