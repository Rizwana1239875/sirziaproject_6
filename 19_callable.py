class Myclass:
    def __call__(self):
        pass
    print("I am callable!")

obj = Myclass
obj() # this will call the __call__ method of Myclass

# checking if an object is callable

def my_function():
    pass
print(callable(my_function)) # True because my_function is callable

class MyClass:
    def __call__(self):
        pass
obj = MyClass()
print(callable(obj)) # True because obj is an instance of MyClass which has __call__ method

print(callable("Hello")) # False because string is not callable
print(callable(123)) # False because integer is not callable
print(callable([1,2,3,4,5])) # False because list is not callable
print(callable(None)) # False because None is not callable
print(callable(MyClass)) # True because MyClass is a class and classes are callable