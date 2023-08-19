# Generate heads or Tails by using random module.
import random

random_flip = random.randint(0,1)
print(random_flip)
if(random_flip == 1) :
    print("Heads")
else :
    print("Tails")