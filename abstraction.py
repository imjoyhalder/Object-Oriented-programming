from abc import ABC,abstractmethod
class shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    # when we make abstractmethod 
    # We can not make it's object
    @abstractmethod
    def area(self):
        pass

class Triangle(shape):
    def area(self):
        area = 0.5*self.dim1*self.dim2
        return f"Triangle area is {area}"

class Rectange(shape):
    def area(self):
        area = self.dim1*self.dim2
        return f"Rectange area is {area}"


object = Triangle(50,34)
print(object.area())
obj1 = shape(49,90)
print(obj1.area())