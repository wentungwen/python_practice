def logging_decorator(function):
   def wrapper(*args):
       result = function()
       print(f"You called {function.__name__} with {args} and result is {result} ")
   return wrapper


@logging_decorator
def a_function(*args):
   num = 1
   for n in args:
       num *= n
   return num


a_function(2, 3, 4)

# You called a_function with (2, 3, 4) and result is 24 