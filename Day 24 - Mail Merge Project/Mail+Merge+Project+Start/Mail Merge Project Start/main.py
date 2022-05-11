# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as letter:
    with open("./Input/Names/invited_names.txt") as names:
        list_letter = letter.readlines()
        list_names = names.readlines()
        title_names = []

        for name in list_names:
            title_names.append(name.replace("\n", ""))

        for replace_name in title_names:
            with open(f"./Output/ReadyToSend/{replace_name}.txt", mode="w") as new_letter:
                string = "".join(list_letter)
                new_string = string.replace("[name]", replace_name)
                new_letter.write(new_string)


