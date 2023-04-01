class Base1:
    def __init__(self):
        self.x = 10
# creating a private variable named y
    def __init__(self):
        self.__y = 5
class Derived1(Base1):
    def __init__(self):
        self.z = 20
        Base1.__init__(self)
ob1 = Derived1()
print(ob1.x)