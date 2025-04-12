"""Dog module

This module does ... bla bla bla and provides following classes:

- Dog
...
...
   
"""


class Dog:
    """A class representing the dog"""
    def __init__(self, name, age):
        """Initialize a new dog

        Args:
            name (str): Dog name
            age (int): Dog age
        """
        self.name = name
        self.age = age
        
    def bark(self):
        """Let the dog bark"""
        print('WOF!')
        
        
        
        
        
def increment(n: int) -> int:
    """Increment a given number by 1

    Args:
        n (int): Initial number
        
    Returns: 
        Incremented number by 1
        
    Raises:
        AnyError: If anything bad happens.
    """
    return n + 1


print(help(Dog))