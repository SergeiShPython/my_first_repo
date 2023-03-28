class Soda():
    def __init__(self,x):
        self.x = x
        y = isinstance(self.x, str)
        if y != True:
            self.x = None

    def shom_my_drink(self):
        if self.x == True:
            print(f"Газировка и ", self.x)
        else: print("Газировка без ничего")

drink = Soda('Кола')
drink.shom_my_drink()

class NoSugar():
    def __init__(self,x=0, sugar=0):
        super().__init__(x)
        self.sugar = sugar

    def is_sugar(self):
        if self.sugar<1:
            print(f"Без сахара, количество сахара {self.sugar}")
        else: print(f"С сахаром, количество сахара {self.sugar}")

drink_sugar = NoSugar("Кола", 1.3)
drink_sugar.is_sugar()
