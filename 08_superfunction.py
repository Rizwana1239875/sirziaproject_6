# Step 1: Parent class
class Person:
    def __init__(self, name):
        self.name = name

# Step 2: Child class
class Teacher(Person):  # inheriting from Person
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject  # super() calls the parent class constructor

    # Step 3: Display method
    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}")

# Step 4: Main block for testing
if __name__ == "__main__":
    # Creating an object of the child class
    teacher = Teacher("Gul", "English")
    # Calling the display method
    teacher.display()
