from itertools import zip_longest
names = input()
cars = input()
sort_names = names.split()
sort_cars = cars.split()
print(sort_names)
print(sort_cars)
sort_names.sort()
sort_cars.sort()
if len(sort_names)!=len(sort_cars):
    print("Машин хватит не на всех")
else:print(list(zip(sort_names, sort_cars)))