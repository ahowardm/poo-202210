class Student:
    def __init__(self, name, family_name, age):
        self.first_name = name
        self.last_name = family_name
        self.age = age
    
    def greet(self):
        # return 'Hello, my name is ' + self.first_name
        return f'Hello, my name is {self.first_name}'