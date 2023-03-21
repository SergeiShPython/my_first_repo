#2. Напишите программу принимающую на вход список [1,2,3] и выводящую все возможные комбинации его членов.:
#Ответ: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)
lst = [1, 2, 3]
variable_lst = []
variable_lst.append([lst[0], lst[1], lst[2]])
variable_lst.append([lst[0], lst[2], lst[1]])
variable_lst.append([lst[1], lst[2], lst[0]])
variable_lst.append([lst[1], lst[0], lst[2]])
variable_lst.append([lst[2], lst[0], lst[1]])
variable_lst.append([lst[2], lst[1], lst[0]])
print(variable_lst)

def