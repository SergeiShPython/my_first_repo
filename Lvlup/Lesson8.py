from math import sqrt
class Rocket():
    def __init__(self, x=0, y=0):
        # Each rocket has (x,y) position
        self.x = x
        self.y = y
    def move_rocket(self, x_increment=0, y_increment=0 ):
        self.y += x_increment
        self.x += y_increment

    def get_distance(self, other_rockets):
        distance = sqrt((self.x - other_rockets.x)**2+(self.y-other_rockets.y)**2)
        return distance
rocket_0 = Rocket()
rocket_1 = Rocket(10, 5)
distance = rocket_0.get_distance(rocket_1)
print(distance)
'''my_rocket = Rocket()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)'''
'''
rockets = [Rocket() for x in range(0,5)]

for rockets in rockets:
    print("Rocket altitude:", rockets.y)

rockets[0].move_rocket()
rockets[1].move_rocket(10,10)
rockets[2].move_rocket(-10,0)


for index , rocket in enumerate(rockets):
    print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))
'''

#a= 1.9
#print(isinstance(a,int))
#lst = [1,2,3,4,'acasd',5,6,777,788]
#print(all(lst))
















