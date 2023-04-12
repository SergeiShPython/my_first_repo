def add(x,y):
    return x+y

print(add(2,3))
###########
add2 = lambda x, y: x+y
print(add2(3,3))
########
def multipy(x):
    return x*2
print(list(map(multipy, [1,2,3,4])))    #MAP(действие, итерируемый объект)

print(list(map(lambda x: x*2, [1,2,3,4])))

list1= [1,2,3,4]
list2= [10,11,12,30]
print(list(map(lambda x,y: x+y , list1, list2)))

a = [1,2,3,4,5,6]
filter(lambda x: x%2 == 0 ,a)

dictionary = [{'name': "python", "points":10}, {'name': "java", "points":8}]
print(list(filter(lambda x:x['name']=='python', dictionary)))
