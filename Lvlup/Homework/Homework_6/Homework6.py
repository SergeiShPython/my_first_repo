"""1.Определите класс Person().
В функции init() определите несколько атрибутов человека. Хорошими атрибутами, которые следует учитывать, являются имя, возраст, место рождения и все,
 что вам нужно знать о людях в вашей жизни. Не менее 3 атрибутов.
Напишите один метод. Это может быть просто introduce_yourself(). Этот метод выводит такое утверждение, как «Здравствуйте, меня зовут Эрик».
Вы также можете создать такой метод, как age_person(). Простая версия этого метода просто добавит 1 к возрасту человека.
Создайте человека, установите соответствующие значения атрибутов и выведите информацию о человеке.
Вызовите свой метод для человека, которого вы создали. Убедитесь, что ваш метод выполняется правильно; если метод ничего не выводит напрямую,
 напечатайте что-нибудь до и после вызова метода, чтобы убедиться, что он сделал то, что предполагалось.
2.Студенческий класс
Начните с вашей программы из класса Person.
Создайте новый класс под названием Student, который наследуется от Person.
Определите некоторые качества, которые есть у учащегося, которых нет у других людей. У учащегося есть школа, с которой он связан, год выпуска,
средний балл и другие особые атрибуты.
Создайте объект Student и докажите, что вы правильно использовали наследование.
Установите некоторые значения атрибутов для учащегося, которые закодированы только в классе Person.
Установите некоторые значения атрибутов для учащегося, которые закодированы только в классе учащегося.
Выведите значения для всех этих атрибутов."""

class Person():
    def __init__(self,name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.birth_place = "Russia"

    def introduce_yourself(self):
        return "Здравствуйте, меня зовут %s %s, мне %s, я родился в %s  " %(self.name, self.surname, self.age, self.birth_place)
    def age_person(self):
        return "в следующем году мне исполнится %s "%(self.age + 1)
human1 = Person("Эрик", "Иванов", 38)
print(human1.introduce_yourself())
print(human1.age_person())

class Student(Person):
    def __init__(self,school, classroom, gpa):
        super().__init__(name="Виктор", surname="Петров", age=17)
        self.school = school
        self.classroom = classroom
        self.gpa = gpa

    def students_introduce_yourself(self):
        return "я учусь в %s,  в %s классе, мой средний бал составляет:%s" %(self.school, self.classroom, self.gpa)

student = Student(12,"9a", 4)
print(student.introduce_yourself())
print(student.age_person())
print(student.students_introduce_yourself())
print(student.name)
print(human1.students_introduce_yourself)