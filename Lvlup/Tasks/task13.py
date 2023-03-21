n = int(input())
l =[]
for i in range(n):
    for j in range(n):
        l.append(n)
    n = n - 1
k = [i for i in l[::-1]]
print(k)