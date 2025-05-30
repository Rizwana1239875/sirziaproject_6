class ObjectCounter: # step2
    def __init__(self,cls):
        print("Decorator Applied:", cls)
        self.cls = cls
        self.count = 0
    def __call__(self, *args,**kwargs):
            self.count += 1
            print(f"{self.cls.__name__} object created {self.count} times")
            return self.cls(*args, **kwargs)
        

@ObjectCounter# step3
class Animal: # step1
    pass
    

a = Animal()
b = Animal()


@ObjectCounter
class Car:
    pass

car1 = Car()
car2 = Car()
car3 = Car()
