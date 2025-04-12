from datetime import datetime

# this is comment
# name = "Volodymyr"
# age = 37

# print(type(name) == str)
# print(isinstance(name, str))
# print(isinstance(age, int))

# print(isinstance(age, float))
# age = float(37)
# print(isinstance(age, float))


# class Dog:
#     def __init__(self):
#         pass

# dog = Dog()
# dog2 = Dog()
# print(isinstance(dog, Dog))


#//* Ternary operator
# def is_adult(age):
#     return True if (age > 18) else False

# print(is_adult(17))


#//* Multiline Strings
# print("""Dog is

# 5

# years old.
# """)

#//* STRING METHODS
""" text = "my doG IS 6 years OLd   "

methods = ['strip', 'lower', 'upper', 'capitalize', 'title', 'swapcase']

for method_name in methods:
    method = getattr(text, method_name)
    result = method()
    print(f"{method_name}: {result}")
    
print("person".islower())

print("one two three".split())

print(" ".join(["one", "two", "three"])) """

#//* ESCAPING CHARACTERS
""" phrase = "This is a \"miracle\""
phrase = 'This is a "miracle"'
phrase = 'This is a \n"miracle"'

print(phrase) """

#//* Indexes and Slicing
""" name = 'Volodymyr'
print(name[0]) # V
print(name[-1]) # r
print(name[1:3]) # ol
print(name[2:6]) # lody
print(name[2:]) # lodymyr
print(name[:6]) # Volody """

#//* Booleans
""" done = True
# done = False
if done:
    print("yes")
else:
    print("no")
"""

#//* ANY ALL
""" 
book_1_read = True
book_2_read = False
read_any_book = any([book_1_read, book_2_read])
print(read_any_book)  # True

read_any_book = all([book_1_read, book_2_read])
print(read_any_book) # False """

#//* Complex numbers
""" complex_num1 = 2 + 3j
complex_num2 = complex(2, 3)

print(complex_num1, complex_num2)
print(complex_num1.real, complex_num2.imag) # 2.0 3.0 """


#//* BUILD-IN FUNCTIONS
""" print(abs(-5.5)) # 5.5
print(round(5.5)) # 6
print(round(5.4)) # 5
print(round(5.49, 1)) # 5.5 """


#//* USER INPUT
""" current_year = datetime.now().year

age = input("What is your age?\n")
result = "You was born in 20th century" if (current_year - int(age)) < 2000 else "You was born in 21st century"
print(f"Your age is {age}. {result}") """

#//* CONTROL STATEMENT
condition = False

if condition:
    print("The condition was true")
else:
    print("The condition was False")