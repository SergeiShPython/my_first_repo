import random
y = True
while y == True:
    answear = input("Кинуть кубики?:")
    if answear == "y":
        print(random.randint(1, 6))
        print(random.randint(1, 6))
    else: y = False