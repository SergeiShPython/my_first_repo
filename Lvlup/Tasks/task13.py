n = int(input())
l =[]
while n>0:
    for i in range(n):
        l.append(n)

        for j in range(n):
            l.append(n)
        n = n - 1
print(l)