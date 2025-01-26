from parent_hierarchical import Parent

class Child2(Parent):
    def func3(self):
        print("This is function is in child2 class")
        
object2 = Child2()
object2.func1()
object2.func3()