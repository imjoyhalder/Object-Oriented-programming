class Fish: 
    def __init__(self):
        self.__size = "big"
    def get_sized (self):
        print("I am a " +self.__size +" fish")
    def set_size(self,new_size):
        self.__size = new_size

 
oscar = Fish()
oscar.get_sized()
# Change the size 
vert =  Fish()
vert.__size = "small"
vert.get_sized()
new_size = Fish()
new_size.get_sized()