# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./Input/Letters/starting_letter.txt") as note:
    contents = note.read()

with open("./Input/Names/invited_names.txt") as names:
    letter_names = names.readlines()

updated_names = []
for string in letter_names:
    the_name = string.strip()
    updated_names.append(the_name)

for name in updated_names:
    new_file = f"./Output/ReadyToSend/letter_for_{name}.txt"
    with open(new_file, mode='w') as new_letter:
        new_letter.write(contents.replace("[name]", name))

