#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 

total_bill = input("enter the bill amount : ")
standard_tip = input("choose the tip among the 10%, 12%, 15% : ")
tip_in_percent = int(standard_tip)/100
customers_num = input("enter the number of customers : ")

bill_per_person = float(total_bill)/float(customers_num)
total_bill_tip = bill_per_person * tip_in_percent

print(f"The payable amount for each customer is {total_bill_tip}")