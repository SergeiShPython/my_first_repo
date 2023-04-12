"""# def return_fun(n):
#     for y in range(0,n):
#         return y
# print(return_fun(10))
#
def generator(n):
    for y in range(0,n):
        yield y
#return_res = return_fun(55)
my_range = generator(10)
#print(list(my_range))
#
# for i in generator(10):
#     print(i)

new_range = generator(3)
print(next(new_range))
print(next(new_range))"""


