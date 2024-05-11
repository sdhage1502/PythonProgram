class mobile:
    def show(self):
        print("This is parents of all mobile")

class realme:
    def show1(self):
        print("This is realme phone")

class narzo(mobile,realme):
    def show2(self):
        print("This is narzo phone")

c=narzo()
c.show()
c.show1()
c.show2()
