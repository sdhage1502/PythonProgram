class student:
    def __init__(self,name):
        print("Constructor created")
        self.name=name
    def show(self):
        print(f"my name is {self.name}")

    def __del__(self):
        print("Destructor called")
c=student("vikas")
c.show()
del c

