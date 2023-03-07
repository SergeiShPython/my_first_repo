squares= [1, 4, 9, 16, 25]
names=['Romeo', 'Kevin', 'Eden', 'Jan', 'Mickey']
print(names[3])
del names[0]        #удаляет пермое значние в массиве
print(names)
names.append(3)         # добавляет в конец 3
print(names)
print(names[1][1])                # [обращение к элементу 1] [обращение к элементу 1 элемента 1]
names.remove("Jan")              # удалет  удакляет первое встретившееся значние
names.pop([0])                   # удаляет элемент по индексу
print(names.index("Jan"))        # выводит индекс джен первой попавшейся
names = ["1", "2", "0"]
names.sort(reverse=True)         # сортирует список и писать до принта reverers в обратную сторону
print(names)
