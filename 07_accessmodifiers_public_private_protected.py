class Employee:
    def __init__(self, name, salary, ssn): #ssn means social security number
        self.name = name         # Public variable
        self._salary = salary    # Protected variable
        self.__ssn = ssn         # Private variable

if __name__ == "__main__":
    emp = Employee("Ali", 60000, "123-45-6789")
    
    # Accessing public variable
    print("public variable:", emp.name)
    
    # Accessing protected variable
    print("protected variable:", emp._salary)
    
    # Accessing private variable
    try:
        print("private variable:", emp.__ssn)  # This will cause an error
    except AttributeError as e:
        print("Error accessing private variable:", e)

    # Accessing the private variable correctly
    print("private variable (correct way):", emp._Employee__ssn)
