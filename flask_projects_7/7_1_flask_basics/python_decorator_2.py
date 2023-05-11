# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        result = function(*args)
        print(f"You called {function.__name__} with {args} and result is {result} ")
    return wrapper


# Use the decorator
@logging_decorator
def a_function(*args):
    num = 1
    for n in args:
        num *= n
    return num


a_function(2, 3, 4)

# class User:
#     def __init__(self, username):
#         self.name = username
#         self.is_logged_in = True
#         self.is_member = False
#
#
# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in:
#             function()
#     return wrapper
#
#
# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"this is {user.name}'s new blog post.")
#
#
# new_user = User("wentung")
# new_user.is_logged_in = True
# create_blog_post(new_user)
