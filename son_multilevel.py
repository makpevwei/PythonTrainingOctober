from father_multilevel import Father

class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        super().__init__(fathername, grandfathername)
        
    def print_name(self):
        print(f"My name is {self.sonname}. My father's name is {self.fathername} and my grandfather's name is {self.grandfathername}")
        
        
son1 = Son("John","Mike","Henry")
son1.print_name()