def logtime(func):
    def wrapper():
        #//% do something before
        print("before")
        func()
        #//% do something after
        print("after")
    return wrapper


@logtime
def hello():
    print("Hello")
    
    
hello()