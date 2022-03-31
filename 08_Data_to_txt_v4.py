# Source: http://www.quru99.com/reading-and-writing-files-in-python.html

import re

has_error = "yes"
while has_error == "yes":
    print()
    filename = input("Enter a filename: ")
    has_error = "no"

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == " ":
            problem = "(no spaces allowed)"
        else:
            problem = f"(no {letter}'s allowed)"
        has_error = "yes"

    if filename == "":
        problem = "can't be blank"
        has_error = "yes"

    if has_error == "yes":
        print(f"Invalid filename = {problem}")
    else:
        print("You entered a valid filename")
