from random import randint
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

class Shuttle(Rocket):
    def __init__(self, x=0, y=0, flights_completed = 0):
        super().__init__(x,y)
        self.flights_completed = flights_completed
shuttles =[]
for i in range(0,3):
    x = randint(0,100)
    y = randint(1, 100)
    flights_completed = randint(0,10)
    shuttles.append(Shuttle(x,y,flights_completed))
rockets = []
for i in range(0,3):
    x = randint(0,100)
    y = randint(1, 100)
    rockets.append(Shuttle(x,y))
for index, shuttle enumerate(shuttles):
    print(index, shuttle.flights_completed)
print('\n')
for index, shuttle in enumerate(shuttles):
    distance = first_