class Student:
    def __init__(self, name="Mike", grade=100, age=30):
        self.name = name
        self.grade = grade
        self.__age = age
        
    def studentdata(self):
        print(f"Name: {self.name} Grade: {self.grade} Age: {self.__age}")
        
s1 = Student()
s2 = Student("Mary", 90)

s1.studentdata()