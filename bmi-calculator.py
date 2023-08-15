# Enter he height and weight values 
height = input("enter yor height in m : ")
weight = input("enter yor weight in kgs : ")

# determine the types of height and weight
height_num = float(height)
weight_num = int(weight)
# Calculating BMI calculator by PEMDAS rule
bmi_number = print(int(weight_num/(height_num**2)))