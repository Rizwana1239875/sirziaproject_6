
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):  # instance method
        print(f"{self.name} is saying Woof!")
if __name__ == "__main__":
        my_dog = Dog("Dogi", "Pakistani   Shepherd")  # creating an object/instance
        # call the instance method
        my_dog.bark()
pass
