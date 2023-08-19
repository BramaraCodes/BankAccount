import random

random.seed(1)

set_state = random.setstate()
print(random.setstate(set_state))