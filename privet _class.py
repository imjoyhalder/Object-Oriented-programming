class _PrivateClass:
    def __init__(self):
        self.private_var = "This is a private variable"

    def _private_method(self):
        print("This is a private method")

class PublicClass:
    def __init__(self):
        self.private_obj = _PrivateClass()

    def use_private(self):
        print(self.private_obj.private_var)
        self.private_obj._private_method()


obj = _PrivateClass()
obj._private_method()

obj1 = PublicClass()
# Here we can see that this object is the privet
obj1.use_pirvate()
