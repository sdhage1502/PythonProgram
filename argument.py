#postional
def add(a,b):
    return a+b
print("Sum is: ",add(5,5))

#keyword
def add(a,b):
    return a+b
print("Sum is: ",add(b=7,a=5))

#default
def add(a=6,b=6):
    return a+b
print("Sum is: ",add())