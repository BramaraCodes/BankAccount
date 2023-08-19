import random
# Roulette is getting started and entering all the friends names
friends = input("Gimme everybody's names, those are at table...\n")
# This can be slip the list into staructure List
names = (friends.split(", "))

# To know the lenght of the List
names_length = len(names)
print(names_length)

# Returns the random person within the List
random_pick = random.randint(0, names_length - 1)
random_person = names[random_pick]
print(f"{random_person} is going to pay for the whole bill....")