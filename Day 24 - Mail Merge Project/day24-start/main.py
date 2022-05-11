with open("../../../my_text.txt") as file:
    contents = file.read()
    print(contents)

with open("text.txt", mode="a") as file:
    file.write("\nTesting")
