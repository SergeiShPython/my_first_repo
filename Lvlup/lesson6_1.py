import random
#print(random.randint(1, 6))
#print(random.uniform(1, 6))
from collections import Counter
#lst = ['apple', 'peach', 'banana', 'srawberry', 'apple']
#print(Counter(lst))
lst = []
for i in range(1000):
    lst.append(random.randint(1, 6))
print(Counter(lst))
