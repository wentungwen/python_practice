# file = open("my_text.txt")
# context = file.read()
# print(context)
# file.close()


# with open("my_text.txt") as file:
#     context = file.read()
#     print(context)

# with open("my_text.txt", mode="r") as file:
#     file.write("New Textttt.")
    # get alert because "r" is read-only

# with open("my_text.txt", mode="w") as file:
#     file.write("New Textttt.")
#     write and replace everything in that file

with open("../../../../Desktop/testt.txt", mode="a") as file:
    print(file.read())

with open("./") as file:
    print(file.read())