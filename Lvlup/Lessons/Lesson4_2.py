string="Outher"
def set():                  # функциря  позволяет делать что то внутри ее и потом это вызвать по имени функции
    #global string           # глобал делает так что бы переменная  затрагивалась и за функцией
    #nonlocal string         # делает так что бы переменная  затрагивалась на 1 уровень выше функции
    string="Inner"
    print(string)
set()
print(string)

def hello(name, prefix="Hello ", suffix = "!"):
    print("{}{}{}".format(prefix, name, suffix))
hello("Anton")

def append_default(element, lst=[]):
    lst.append(element)
    return lst
print(append_default("1"))
print(append_default("2"))

def printc(arg1, arg2, *args, **kwargs):                #*args вбирает в себя все лишние переменные без явного указания имени переменное **kwargs вбирает в себя все переменные с именами
    print(" ".join([arg1]+[arg2]+list(args)+list(kwargs.values())))
printc('1', '2', '3', four="4", five="5")
