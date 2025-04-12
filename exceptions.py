""" try:
    # some lines of code
except <ERROR1>:
    # handles <ERROR1>
except <ERROR2>:
    # handles <ERROR2>
else:
    # no exceptions were raised, the code ran successfully
finally:
    # do something in any case """
    

""" try:
    result = 2 / 0
    print(result)    
except ZeroDivisionError:
    print("Division by zero not allowed!")
finally:
    result = 1
    
print(result) # 1 """


""" try:
    raise Exception("An error occurred while executing the command.")
except Exception as error:
   print(error) """
   
   
#//% Custom exception class

class DogNotFoundException(Exception):
    print("Sorry")
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
   print("Dog not found!")