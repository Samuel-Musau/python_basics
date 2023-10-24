class students:
    def __init__(self,name,course,gender,age):
        self.name=name
        self.course=course
        self.gender=gender
        self.age=age
    def wanafunzi(self):
        print("Name: %s \nCourse: %s \nGender: %s \nAge: %d" %(self.name,self.course,self.gender,self.age))

stud1=students("erick", "comp science", "male" 30)
stud1.wanafunzi()
stud2=students("ann", "software engineering", "female" 25)
stud2.wanafunzi()

stud3=students("sam","comp sci", "male", 22)
stud3.wanafunzi()
stud4=students("manex", "data science", "male" 28)
students.wanafunzi()
