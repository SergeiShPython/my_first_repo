class Soda():
    def __init__(self, x):
        self.x = x
        y = isinstance(self.x, str)
        if y != True:
            self.x = None

    def shom_my_drink(self):
        print("Газировка и %s" % (self.x))
dobavka = input()
drink = Soda.shom_my_drink(dobavka)
print(drink)


