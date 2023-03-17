contribution = int(input("Введите предполагаемый вклад: "))
term = int(input("Введите срок в ГОДАХ!)): "))
percent = float(input("Введите процентную ставку: "))
result = float()
def my_bank():
    result = contribution * ((1+(percent/100))**term)
    return result
print(my_bank())