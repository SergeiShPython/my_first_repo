string = input()
lst = string.split()
#lst = [16 , 23 , 78, 99]
def change(lst):
    t = lst[0]
    lst[0] = lst[-1]
    lst[-1] = t
    return lst
print(change(lst))
