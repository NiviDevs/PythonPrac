class Details:
    def __init__(self,name,regno):
        self.name = name
        self.reg = regno

class Staff(Details):
    pass
class Student(Details):
    pass
#Example usage
stu1 = Student("Nevedya","24BEC0431")
print(stu1.name)