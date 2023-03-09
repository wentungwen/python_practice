
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("message")
except KeyError as error_message:
    print(error_message)
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")

x = 5
if x > 3:
    raise ValueError("I made this error.")
