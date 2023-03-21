#5. Напишите функцию которая принимает на вход неограниченное количество аргументов, а на выходе возвращает их сумму. Используйте *args.
def sum_of_elem(*args):
    summ = sum(args)
    print("Сумма аргументов равна:", summ)
sum_of_elem(1,2,3,4,6,43,56,6,7,3,345)



import random
lst = [random.randint(0,100 ) for i in range(random.randint(2,30))]
print(lst)
def summa(*args):
    print("Сумма аргументов равна:", sum(args))
summa(*lst)
