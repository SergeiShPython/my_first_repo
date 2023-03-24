#1. Напишите программу, принимающую на вход слова через запятую и выводящую слова в алфавитном порядке. Используйте List comprehension.
lst = input().lower()
sort_lst = sorted([i for i in lst.split(",")])
print(sort_lst)