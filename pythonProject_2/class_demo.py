class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("I'm alive")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print(f"in the water {self.num_eyes}")

    def swim(self):
        print("move faster")


nimo = Fish()
nimo.breathe()
# class User:
#
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         self.following += 1
#         user.followers += 1
#
#
# user_1 = User("1", "Angel")
# user_2 = User("2", "Andy")
#
# user_1.follow(user_2)
# print(user_2.followers, user_1.following)