# student 1
s1_name="Usman"
s1_marks=85
s1_DateOfBirth=5-11-2003

# student2
s2_name="Habiba"
s2_marks=80
s2_DateOfBirth=30-5-2005

def calculate_grade(marks):
    if marks>=90:
        return("A")
    elif marks>=75:
        return("B")
    else:
        return("C")

def updated_marks(old_marks,new_marks):
    return new_marks

print("student 1 name",s1_name)
print("Student 1 marks",s1_marks)
print(" grade:",calculate_grade(s1_marks))

print("student 2 name",s2_name)
print("Student 2 marks",s2_marks)
print("student 2 grade", calculate_grade(s2_marks))

s1_marks=updated_marks(s1_marks,99)
print("student 1 name",s1_name)
print("Student 1 marks",s1_marks)
print("student 1 grade", calculate_grade(s1_marks))

# before oop
# programming = instruction +loose data
# no protection of data anyone can change the student info and access it
# no scaling
# function dont belong anywhere
# large obj become messy hard to organize


# afer oop
# data grouped in obj ,data belongs to an obj ,organized data
# add new data feature 
# less complexity understandale
# programming = interacting objs

