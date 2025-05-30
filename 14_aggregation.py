class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee # aggregation

    def show_employee(self):
        print(f"Employee in department: {self.employee.name}")

if __name__ == "__main__":
    emp = Employee("Ali")
    dept = Department(emp)
    dept.show_employee()

    del dept
    #print(dept)
    print(emp)
             
        