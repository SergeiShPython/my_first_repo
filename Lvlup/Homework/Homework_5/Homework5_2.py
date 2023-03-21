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

#способ 2(для извращенцев)
lst2 = [1, 2, 3]
def output_lst2(lst2):
    out_list = []
    x = []
    y = []
    out_list.append(lst2)
    lst3 = [i for i in lst2[::-1]]
    out_list.append(lst3)
    for i in range(len(lst2)):
        if lst2[i] != lst3[i]:
            x.append(lst2[i])
        for i in range(len(x)):
            if x[i] != lst2[i]:
                x.append(lst2[i])
    out_list.append(x)
    for i in range(len(lst2)):
        if lst2[i] != lst3[i]:
            y.append(lst3[i])
        for i in range(len(y)):
            if y[i] != lst3[i]:
                y.append(lst3[i])
    out_list.append(y)
    z = [i for i in x[::-1]]
    out_list.append(z)
    k = [i for i in y[::-1]]
    out_list.append(k)
    return out_list
print(output_lst2(lst2))


