i = int(input())
def year(i):
   if i%4 == 0 and i%400 == 0 and i%100 != 0:
       return "високосный"
   else: return "не високосный"
print(year(i))