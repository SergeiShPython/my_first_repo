import random
from collections import Counter
lst = []
for i in range(1000):
    lst.append(random.randint(1, 6))
print(Counter(lst))

#lst = [append(random.randint(1, 6) for i in range(1000)]