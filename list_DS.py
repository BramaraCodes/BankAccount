# Data structures : List type

fruits = ["apples", "bananas", "oranges", "kiwis", "longans", "sapodalias"]
# Offset or index starts from begining of the List
print(fruits[1])

# Offset or index starts from begining of the List
print(fruits[-1])

# This changes the fruits inside the list
fruits[5] = "sapota"
print(fruits)

# Appending a fruit at the en of the list
fruits.append("tomato")
print(fruits)

# Extension for existing list.
fruits.extend(["grapes", "mangosteen", "drangonfruit", "litchie", "watermelon"])
print(fruits)