# Pizza order program to deliver small, medium and large pizza.

print("Welcome to The MamaMia's Pizza")

pizza_order = input("Select the pizza you like : Small, Medium and Large\n")

if(pizza_order == "Small") :
    bill = 15 
    print("Small Pizza : 15$")
elif(pizza_order == "Medium"):
    bill = 20 
    print("Medium Pizza : 20$")
else :
    bill = 25 
    print("Large Pizza : 25$")

extra_toppings = input("Please select the below delicious toppings on Pizza : Yes or No. \n")

if(extra_toppings == "Yes") :
    extra_cheese = input("Do you like extra cheese on top? Yes or No. \n")

    if(extra_cheese == "Yes") :
        bill += 1          
    extra_pepperoni = input("Do you like pepperoni on pizza? Yes or No. \n")
    if(extra_pepperoni == "Yes") :
        select_toppings = input("Select the toppings : 'Pepperoni for Small' or 'Pepperoni for Medium or Large'. \n")
        if(select_toppings == "Pepperoni for Small") :
            bill += 3
            print(f"Total bill is {bill}$ for small pizza")
        elif(select_toppings == "Pepperoni for Medium or Large"):
            bill += 5 
            print(f"Total bill is {bill}$ for medium or Large pizza")
        else :
            print(f"Thanks for the order, total bill is {bill}$")
else:
    print(f"Thanks for the order. Your total bill is {bill}$")