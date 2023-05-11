import time


# Functions can have inputs/functionality/output
# Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(function, num1, num2):
    return function(num1, num2)


print(calculator(divide, 2, 4))


# Functions can be nested in other functions
def outer():
    print("Hi,")

    def nested():
        print("hello!")

    nested()


outer()


# Functions can be returned from other functions
def outer():
    print("Hi,")

    def nested():
        print("hello!")

    return nested


inner = outer()
inner()


# Simple Python Decorator Functions
def delayed_decorator(function):
    def wrapper_func():
        time.sleep(2)
        function()

    return wrapper_func


@delayed_decorator
def say_ok():
    print("ok")


def say_bye():
    print("bye")


# Method 1: using syntactic sugar
say_ok()
say_bye()

# Method 2: calling the functions
decorated_ok = delayed_decorator(say_ok)
decorated_ok()
decorated_bye = delayed_decorator(say_bye)
decorated_bye()



# Calling multiple decorators

def my_decorator(func):
    def wrapper1():
        print("Before the function is called.")
        func()
        print("After the function is called.")

    def wrapper2():
        print("Another wrapper function.")

    return wrapper1, wrapper2


@my_decorator
def say_hello():
    print("Hello!")


wrapper1, wrapper2 = my_decorator(say_hello)

wrapper1()  # Output: Before the function is called. Hello! After the function is called.
wrapper2()  # Output: Another wrapper function.
