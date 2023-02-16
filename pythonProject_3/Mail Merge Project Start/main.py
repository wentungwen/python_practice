# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as name_file:
    names = name_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt", "r") as template_file:
    contents = template_file.read()
    print(contents)

    for name in names:
        stripped_name = name.strip()
        new_content = contents.replace(PLACEHOLDER, stripped_name)
        print(new_content)
        with open(f"Output/ReadyToSend/letter_{stripped_name}.txt", "a") as ready_to_sent:
            ready_to_sent.write(new_content)





