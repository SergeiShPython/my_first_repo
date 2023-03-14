i = int(input())
def year(i):
   if i%4 == 0 or i%400 == 0 or i%100 == 0:
       return "высокосный"
   else: return "не высокосный"
print(year(i))