# Random number generator tutorials

"""
It's a random module that can helps us to generates some random integers, 
floats, sequence, bytes, ranges 
"""
import random
# We can import any python random module that is created outside this Python file.
import my_random_module

# random integer selection.
random_integer = random.randint(23,89)
print(random_integer)

# random module is import and we can access the constants or functions from this module.
print(my_random_module.pi)

# Returns the next random floating point number between [0.0 to 1.0)
random_float = random.random()
print(random_float)
# Returns the next random floating point number between [0.0000.. to 4.9999999)
print(random_float*5)

love_score = random.randint(1, 200)
print(f"You're love score is {love_score}")

