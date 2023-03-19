#5. Напишите функцию которая принимает на вход неограниченное количество аргументов, а на выходе возвращает их сумму. Используйте *args.
def sum_of_elem(*args):
    summ = sum(args)
    print("Сумма аргументов равна:", summ)
sum_of_elem(1,2,3,4,6,43,56,6,7,3,345)


#хочу понять как передать значения элементов списка но пока не вышло и можно ли так вообще
"""import random
lst = [random.randint(0,100 ) for i in range(10)]
print(lst)
sum_of_elem([lst[i]for i in range(len(lst))])"""
