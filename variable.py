#instance
class student:
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
    def show(self):
        print(f"Student name is {self.name} and department is {self.dept} ")
s1=student("vikas","mca")
s1.show()
print(s1)

#static
class student:
    dept="mca"
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"Student name is {self.name} and department is {self.dept} ")
s1=student("vikas")
s1.show()
print(s1)

#local
class student:
    name="vikas"
    dept="mca"
    def show(self):
        print(f"Student name is {self.name} and department is {self.dept} ")
s1=student()
s1.show()
print(s1)