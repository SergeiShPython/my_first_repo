my_string= r"Hello \' World"    #слеш что бы поставить специальный символ \" или \\ или \n. r в начале лдя передачи текста как есть
print(my_string[0])             # обращение к 1 символу в строке, [0:-1] обращение от первого к последнему
print(len(my_string))           # выводит длинну строки
for i in range(len(my_string)):
    print(i)
print(my_string.replace("ello","i"))  # имя переменной точка метод, заменяет  что-то на что-то
print(my_string.upper())                # делает буквы заглавными
print(my_string.isdigit())              # проверяет на логическое  тру и фолс
print("My name is {}. My surename is {}". format(1, 2))# {} означает куда вставлять что то, .format  что вставлять
print(f"My name is {name2}. My surename is {name}") # f в начале, подставляет в строки  переменные
print(my_string.count("ll")) # считает сколько раз чего то в строке
print(my_string.split())    # разбивает строку на составляющую. по умолчанию через пробелы

for i in my_string.split("#"):    #передвигаемся по строке разбивая ее по символу #
    i = "#" + i                   # добавляем значению i решотку
    if len(i)>1:                    # если длина i больше 1
        print(i)                    # выводим значения i
