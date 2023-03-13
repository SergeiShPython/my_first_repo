p = int(input("Введите предполагаемый вклад: "))
t = int(input("Введите срок в ГОДАХ!)): "))
i = float(input("Введите проценты: "))
s = float()
def my_bank():
    s = p * ((1+(i/100))**t)
    return s
print(my_bank())



