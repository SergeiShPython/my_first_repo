print("Введите список чисел:")
list_of_inputs = input()
list_of_inputs=[int(num) for num in list_of_inputs]
x=0
for i in list_of_inputs:
    y=list_of_inputs[i+1]
#    for y in list_of_inputs:
    if i != y:
       continue
    else: print(i)

