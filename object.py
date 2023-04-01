class BaseClass():
    def __init__(self):
        print("Base class")

class childClass(BaseClass):
    def __init__(self):
        print("Child class")

class grandchildClass(childClass):
    def __init__(self):
        BaseClass.__init__(self)
        childClass.__init__(self)
        print("Grand child class")

ob1 = grandchildClass()

