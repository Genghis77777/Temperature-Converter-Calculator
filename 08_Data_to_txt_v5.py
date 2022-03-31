# Source: http://www.quru99.com/reading-and-writing-files-in-python.html

import re

data = ['I', 'love', 'computers']

has_error = "yes"
while has_error == "yes":
    has_error = "no"
    filename = input("Enter a filename (leave off extension): ")

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == " ":
            problem = "(no spaces allowed)"

        else:
            problem = f"(no {letter}'s allowed)"
        has_error = "yes"
        break

    if filename == "":
        problem = "can't be blank"
        has_error = "yes"

    if has_error == "yes":
        print(f"Invalid filename = {problem}")
        print()
    else:
        print("You entered a valid filename")

filename = filename + ".txt"

f = open(filename, "w+")

for item in data:
    f.write(item + "\n")

# close file
f.close()
