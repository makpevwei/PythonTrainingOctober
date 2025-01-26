# import person as p
from person import *

class Student(Person):
    def __init__(self, id, fname, lname, age, grade):
        super().__init__(fname, lname, age)
        self.id = id
        self.grade = grade
        
    def display_info(self):
        print(f"My id is {self.id} and my fullnames are {self.firstname} {self.lastname} and I am {self.age} years old and my grade is {self.grade}")
              
            
student1 = Student(101, "John", "Doe", 20, "A")
student1.display_info()  # Output: My id is 101 and my fullnames are John