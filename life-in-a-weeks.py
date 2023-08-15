# Life in a week exercise

present_age = input("enter your current age : ")
# Calculating the years left
present_age_int = int(present_age)
print(present_age_int)
years_left = 90-(present_age_int)

# Calculating days
days_left = years_left * 365
# Calculating weeks
weeks_left = years_left * 54
# Calculating months
months_left = years_left * 12

print(f"Your are left with {days_left} days, {weeks_left} weeks and {months_left} months left.")