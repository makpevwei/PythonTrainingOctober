from mother import *
from father import *

class Son(Mother, Father):
    def __init__(self, mother, father):
        Mother.__init__(self,mother)
        Father.__init__(self,father)
        
    def parents(self):
        print(f"My father's name is {self.father} and my mother's name is {self.mother}")
        
        
son1 = Son("Mary","Alex")
son1.parents()