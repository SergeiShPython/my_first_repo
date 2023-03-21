#1. Напишите программу, принимающую на вход слова через запятую и выводящую слова в алфавитном порядке. Используйте List comprehension.
lst = input().lower()
sort_lst = sorted([i for i in lst.split(",")])
print(sort_lst)


#print(list(map(lambda i : sorted(lst.split(",")),lst))) хотел через лямбду, она даже сортирует и выводит как нужно, но почему-то список выводится очень много  его копий