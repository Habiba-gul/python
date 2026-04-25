# Inheritance means one class (child) can use properties and methods of another class (parent).
# Reuse code
# Avoid repetition
# Create relationships between classes

class Person:
    def __init__(self,name):
        self.name=name
    
    def show(self):
        print("Name",self.name)
        
class Student(Person):   #Inheritance
    def __init__(self,name,rollnumber,grade):
        super().__init__(name)  #super() used to call parent constructor
        self.rollnumber=rollnumber
        self.grade=grade
    
    def display(self):
        print("Roll no",self.rollnumber)
        print("grade :",self.grade)
        
S=Student("Aliha",123,"A")

S.show()
S.display()
        
    
