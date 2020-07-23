class Person:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    # def __repr__(self):
    #     '''
    #
    #     :return: the object representation
    #     '''
    #     return {'name':self.name, 'age':self.age}
    #
    # def __str__(self):
    #     '''
    #     it's called when print() or str() functions are invoked on an object.
    #     :return: the string representation of the object
    #     '''
    #     return 'Person(name='+self.name+', age='+str(self.age)+ ')'

if __name__ == '__main__':

    p = Person('Pankaj', 34)

    print(p.__str__()) # <__main__.Person object at 0x7ff6610f0690>
    print(p.__repr__()) # <__main__.Person object at 0x7ff6610f0690>
    # As you can see above that the default implementation is useless!
    print('`'*5)
    # # __str__() example
    # print(p)
    # print(p.__str__())
    #
    # s = str(p)
    # print(s)
    #
    # # __repr__() example
    # print(p.__repr__())
    # print(type(p.__repr__()))
    # print(repr(p))
