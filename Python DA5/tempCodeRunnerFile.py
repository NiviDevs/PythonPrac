class detail:
    def __init__(self, age):
        self.age = age

p1=detail(input("Enter age of person 1: "))
p2 = detail(input("Enter age of person 2: "))
print("Person 1" if p1.age > p2.age else "Person 2",' is elder')