from restuarant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['a', 'b', 'c']

    def show_flavors(self):
        print('the flavors of ice Cream are: ')
        for flavor in self.flavors:
            print(flavor)


ice1 = IceCreamStand('beijing','China')
ice1.show_flavors()

from random import randint

for i in range(10):
    print(randint(1,6))