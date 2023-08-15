"""
Create a Python program that takes a student's score as input and then 
calculates and prints their corresponding grade based on the following criteria:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60
Here's a template to get you started:

"""

sub_1 = float(input("Enter English subject marks : "))
sub_2 = float(input("Enter Telugu subject marks : "))
sub_3 = float(input("Enter Hindi subject marks : "))
sub_4 = float(input("Enter Maths subject marks : "))
sub_5 = float(input("Enter Science subject marks : "))
sub_6 = float(input("Enter Social subject marks : "))

total_marks = float(sub_1 + sub_2 + sub_3 + sub_4 + sub_5 + sub_6)
print("Your total score in the semister : ", total_marks)

score_grade = (total_marks/100) * 100
if score_grade < 60:
    print("You really need to improve the learning.... and your's grade is F")
elif 60 < score_grade < 69:
    print("Not bad but do some pushups.... and your's grade is E")
elif 70< score_grade < 79 :
    print("Good job.....buddy and  and your's grade is D")
elif 80 < score_grade < 89 :
    print("Congrats champ..you've made it and your's grade is D")
elif score_grade >= 90:
    print("Out of this world.....you've made it to A")
else :
    print("Please enter valid options")