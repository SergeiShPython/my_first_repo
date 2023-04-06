lst = ["aaaa8","bb8","ccc8","dddddd8"]
mylst = map(lambda each:each.strip("8"), lst)
for i in mylst:
    print(i)
print(mylst)