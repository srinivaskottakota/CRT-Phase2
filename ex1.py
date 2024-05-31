class ece:
    def __init__(self,name,id,sgpa,cgpa):
        self.name= name
        self.id= id
        self.sgpa= sgpa
        self.cgpa= cgpa
    def printall(self):
        print(self.name)
        print(self.id)
        print(self.sgpa)
        print(self.cgpa)
obj = ece("Hari", 409, 8.0, 8.5)
obj.printall()
obj1 = ece("harsha",410,7.9,8.0)
obj1.printall()
obj2 = ece("harish",411,7.5,8.2)
obj2.printall()