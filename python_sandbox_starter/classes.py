# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#CREATE CLASS
class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

def greeting(self):
    return f'My name is {self.name} and I am {self.age}'
# INIT USER OBJECT
brennan = User('Brennan Predmore', 'brennnann@gmail.com', 29)

# print(brennan.email)

print(brennan.greeting())