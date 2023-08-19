# Finding The smallest Value in Python!

numbers = [54, 34, 21, 42, 51, 10, 41]

smallest = None

for value in numbers:
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
print(smallest)        







    