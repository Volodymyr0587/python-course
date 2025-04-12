""" def hello(name: str = 'John', age: int = 25) -> None:
    if not name:
        return
    print(f"Hello {name}, you are {age} years old.") """

    
""" hello()
hello("Jack")
hello("Jane", 43)
 """    
    
""" def hello(name: str = 'John', age: int = 25) -> tuple:    
    print(f"Hello {name}, you are {age} years old.")
    return name, age

print(hello("Syd")) """

#//* ===========================================================
#//* VARIABLE SCOPE

""" age = 8

def test():
    print(age)
    
print(age) # 8
test() # 8 """

#//* ===========================================================
#//* NESTED FUNCTIONS
""" 
def talk(phrase):
    def say(word):
        print(word)
        
    words = phrase.split(' ')
    for word in words:
        say(word)
        
talk("I am going to buy the milk")
"""

""" 
def count():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        print(count)
        
    increment()
    
count()
 """
 
#//* ===========================================================
#//* CLOSURES

def counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

increment = counter()

print(increment()) # 1
print(increment()) # 2
print(increment()) # 3
