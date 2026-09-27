#Decorators

def greeting(func):
    def wrapper():
        print("Good morning broh! 👋")
        func()

    return wrapper


@greeting
def welcome():
    print("Welcome to Python!")


welcome()