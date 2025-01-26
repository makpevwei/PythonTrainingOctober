from parent_hierarchical import Parent

class Child1(Parent):
    def func2(self):
        print("This is function is in child1 class")
        
object1 = Child1()
object1.func1()
object1.func2()