lst = input()
sort_lst = sorted([i for i in lst.split(",")])
print(sort_lst)


#print(list(map(lambda i : sorted(lst.split(",")),lst))) хотел через лямбду, она даже сортирует и выводит как нужно, но почему-то список выводится очень много  его копий