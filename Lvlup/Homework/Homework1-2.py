list_of_input = input("Введите список чисел:")
variable = []
for i in list_of_input:
    x = 0
    for j in list_of_input:
        if i == j:
            x += 1
    if x == 1:
        variable.append(i)
print(variable)
# или так
variable2 = []
for u in list_of_input:
    if list_of_input.count(u) == 1:
        variable2.append(u)
print(variable2)