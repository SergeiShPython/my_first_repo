'''from datetime import time, date , datetime
import datetime
now =datetime.datetime.today()

print(now)

d = datetime.date(2023,3, 20)
print(d)
print(d.year)
print(d.month)
print(d.day)
a = time()
print(a)
b = time(11,34,56)

print(b)
print(b.hour)

a= datetime(2023,3,21)
print(a)
b= datetime(2023,3,21 , 10,10,10)
print(b)'''
from datetime import date, time ,datetime, timedelta
t1 = date(2018 ,7 , 12)
t2 = date(2017 ,5 , 4)
t3= t1 -t2
print(t3)
t4 = timedelta(weeks=2, days=3, hours=1, seconds=55)
t5 = timedelta(days=11, minutes=4, seconds=5)

t6= t4-t5

print(t6)
print(t6.total_seconds())

now = datetime.now()
t = now.strftime('%H:%M:%S')
print(t)

s1 = now.strftime('%m:%d:%Y, %H:%M:%S')
print(s1)
