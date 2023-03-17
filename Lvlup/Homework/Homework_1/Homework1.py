print("Введите список чисел:")
num1 = input()
num1 = [int(num) for num in num1]
print(max(num1, key=int))
print(min(num1, key=int))
for i in num1:
   if i%3 == 0 and i%5 != 0:
        print(i)
