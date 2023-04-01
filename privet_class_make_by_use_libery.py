from private import private
try:
    @private
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
    test = PublicClass()
    test.use_private()
except Exception as e:
    print(e)