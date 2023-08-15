# BMI checker
# elif statements

height = float(input("Enter your height in m : "))
weight = int(input("Enter your weight in kgs : "))

# BMI calculator :
height_square = float(height**2) # exponent(height*height)
bmi = (weight/height_square)
total_bmi = float(bmi)

if total_bmi < 18.5:
    print(f"Your BMI is {total_bmi}, you are slightly underweight.")
elif total_bmi < 25:
    print(f"Your BMI is {total_bmi}, you have a normal weight.")
elif total_bmi < 30:
    print(f"Your BMI is {total_bmi}, you are slightly overweight.")
elif total_bmi < 35:
    print(f"Your BMI is {total_bmi}, you are obese.")
else:
    print(f"Your BMI is {total_bmi}, you are clinically obese.")
