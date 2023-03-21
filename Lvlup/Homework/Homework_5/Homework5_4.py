#4. Используя random.sample сгенерируйте список случайных элементов. Используйте List comprehension.
import random
lst = [random.randint(0,100 ) for i in range(10)]
print(lst)
print(random.sample(lst, len(lst)))
lst1 =[random.sample(lst, len(lst)) for i in range(len(lst))]
print(lst1)