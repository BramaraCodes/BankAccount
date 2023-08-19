import random

print("Welcome to the Miniso Store...")
toys = input("Let me know what toys you wanna pick now....")
toys_list = toys.split(", ")

toys_len = len(toys_list)
random_toypick = random.randint(0, toys_len-1)
selected_toy = toys_list[random_toypick]
print(f"You've seected the {selected_toy} from Miniso")