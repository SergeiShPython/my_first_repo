#4. Используя random.sample сгенерируйте список случайных элементов. Используйте List comprehension.
import random
lst = [random.randint(0,100 ) for i in range(10)]
print(random.sample(lst, len(lst)))
lst2 = random.sample([i for i in range(random.randint(1, 1000))], random.randint(0, 30))
print(lst2)
lst3 =[random.sample(lst, len(lst)) for i in range(len(lst))]
print(lst3)