
class Person:
    def __init__(self, name):
        pass
        self._name = name

    @property
    def name(self):
        return self._name
        
person = Person("Ali")
print(person.name) 


class Person:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return(self.name)
    
    @name.setter
    def name(self, new_name):
        self.name = new_name

        # update value
    person = Person("Ali")
    print("Before:", person.name)
    Person.name = "Saba"
    print("After:", Person.name)

    # del Person.name

    @name.deleter
    def name(self):
        print("Deleting name!")
        del self.name

    person = Person("Ali")
    print(Person.name)
    del Person.name

