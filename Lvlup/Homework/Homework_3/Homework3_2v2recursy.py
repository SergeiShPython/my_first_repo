contribution = int(input("Введите предполагаемый вклад: "))
term = int(input("Введите срок в ГОДАХ!)): "))
percent = float(input("Введите процентную ставку: "))
def my_bank(term):
    return 1 if term== 0 else (1+(percent/100))*my_bank(term-1)
my_bank(term)10
def final_contribution(contribution,my_bank):
    return contribution * my_bank
print(f"Ваш вклад составит через {term} года(лет):", final_contribution(contribution,my_bank(term)), "денег")
