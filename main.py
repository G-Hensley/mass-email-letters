# Opens the starting letter template
with open("./Input/Letters/starting_letter.txt") as note:
    contents = note.read()

# Opens the list of names to be invited
with open("./Input/Names/invited_names.txt") as names:
    letter_names = names.readlines()

# Creates a list of names without the new line characters
updated_names = []
for string in letter_names:
    the_name = string.strip()
    updated_names.append(the_name)

# Creates a new file for each name in the list
for name in updated_names:
    new_file = f"./Output/ReadyToSend/letter_for_{name}.txt"
    with open(new_file, mode='w') as new_letter:
        new_letter.write(contents.replace("[name]", name))

