# Decorators.
## Extend or modify the behaviour of 
## functions or without changing their code
## CALLBACKS<-->

#crown <--->
def my_deco(func):
    def wrapper():
        print("Calling hello world function")
        func()
        print("Finished calling hello world")
    
    return wrapper


@my_deco
def hello():
    print("hello world")

@my_deco
def greet():
    print("Greetings from above")

greet()
hello()