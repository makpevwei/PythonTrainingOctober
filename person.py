class Person:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        
    def show(self):
        print(f"Name: {self.firstname} {self.lastname} \nAge: {self.age}")
        
        
person = Person("Mike", "Alex", 30)
person.show()