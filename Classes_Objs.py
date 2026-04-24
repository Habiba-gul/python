#  class---->blue print
# object----> real instance created from class
# --init-- (store data in objs) intitalize obj

class Student:
    #    blue print
    def __init__(self,name,marks,date_of_birth): #self refers to current object
        self.name=name
        self.marks=marks
        self.date_of_birth=date_of_birth

    def calculate_grade(self):
        if self.marks>=90:
            return("A")
        elif self.marks>=75:
            return("B")
        else:
            return ("C")

        
# object
s1=Student("usamn",87,5-11-2003)
s2=Student("misbah",90,16-2010)

print(s1.calculate_grade())

# print(s1.name)   
# print(s2.name)