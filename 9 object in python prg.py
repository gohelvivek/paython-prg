class Person:
    "This is a person class"
    age = 10
    def greet(self):
        print('Hello')
harry = Person()
print(Person.greet)
print(harry.greet)
harry.greet()
