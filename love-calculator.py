"""
Love compatibility score program.
TRUE LOVE, 
Enter his name : Jones
Enter her name : Christina

T : 1 time
R : 1 time
U : 0 time
E : 1 time
Total : 3

L : 0 times
O : 1 times
V : 0 times
E : 1 times
Total : 2

Percentage : 32%

Love score is : 32
Print : Your love score is 32

Cases :
If Love score is less than 10 and greater than 90, then 
    Your score is x, you go together like coke and mentos.
If Love score is between 40 to 50, then you go together like coke and mentos
    Your score is x, you are alright together.
Otherwise :
    Your score is x
"""

"""
Python functions :
"Bramara".lower() : Converts all the letters to lower case.
"Bramara".counts("a") : counts number of "a" in the word given.
"""

his_name = input("Enter his name : \n")
her_name = input("Enter her name : \n")

# converting names into lowercase
lowercase_his_name = his_name.lower()
lowercase_her_name = her_name.lower()

both_names = lowercase_his_name + lowercase_her_name

print(both_names)

# counting letters in the lowercase names with respect to TRUE LOVE.
t = both_names.count("t")
r = both_names.count("r")
u = both_names.count("u")
e = both_names.count("e")
l = both_names.count("l")
o = both_names.count("o")
v = both_names.count("v")
e_e = both_names.count("e")
# Counting letters
true_total = t+r+u+e
love_total = l+o+v+e_e

# Concatenating the strings
love_score = str(true_total) + str(love_total)
love_int_score = int(love_score)
# love_score = int(str(true_total) + str(love_total))

if love_int_score < 10 or love_int_score > 90 :
    print(f"Your score is {love_int_score}, you go together like coke and mentos.")
elif (love_int_score >= 40) and (love_int_score <= 50) :
    print(f"Your score is {love_int_score}, you are alright together.")
else :
    print(f"Your love score is {love_int_score}")

# Result :
"""
My first win....!!!!!!!!!!!!!!!!!!!!!!!!!
"""