lisok =(list(zip([1,2,3], ("XYZ"),
        ("seven", "eight" , "nine"),{0:'zero',1:'one',2:'two',}.values()))) # .values после фигурных скобок позволяет обращаться не к ключам а к значениям
print(lisok)


from itertools import zip_longest
result_list = list(zip_longest([1], 'abcd', (7,8,9), fillvalue= None))
print(result_list)

a = list(range(5))
b = list(range(3,10))
result_list2 = list(zip_longest(a, b, fillvalue="?"))
print(result_list2)