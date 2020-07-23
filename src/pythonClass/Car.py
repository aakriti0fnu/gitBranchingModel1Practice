class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return 'a {self.color} car'.format(self=self)
    # def __repr__(self):

if __name__ == '__main__':
    my_car =Car('red', 37281)
    print(my_car) # <__main__.Car object at 0x7fe51a18da10>
    print(my_car.color, my_car.mileage)
    print(my_car)