dictionary = {1:"Январь(31 день)",
              2:"Февраль(28 дней)",
              3:"Март(31 день)",
              4:"Апрель(30дней)",
              5:"Май(31 день)",
              6:"Июнь(30дней)",
              7:"Июль(31 день)",
              8:"Агуст(31 день)",
              9:"Сентябрь(30дней)",
              10:"Октябрь(31 день)",
              11:"Ноябрь(30дней)",
              12:"Декабрь(31 день)"}
number_of_mounth = int(input("Введите номер месяца:"))
if number_of_mounth < 13 and number_of_mounth > 0:
    print(dictionary[number_of_mounth])
else: print("Вы ввели несуществующий месяц")