class Animal:
    def walk(self):
        print("Walking...")

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print("woof!")
        
        
roger = Dog("Roger", 5)
# print(type(roger))
print(roger.name, roger.age)
roger.bark()

print(roger.__dict__)
print(dir(Dog))

roger.walk()