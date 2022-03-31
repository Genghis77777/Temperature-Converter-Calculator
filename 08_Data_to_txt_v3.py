# Source: http://www.quru99.com/reading-and-writing-files-in-python.html

import re

# Data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Get filename, can't be blank / invalid
# Assume valid data for now.
filename = input("Enter a Filename (leave off the extension): ")

valid_file = "[A-Zaz]"
if re.match(valid_file, filename):

    # Add .txt suffix!
    filename = filename + ".txt"

    # Create file to hold data
    f = open(filename, "w+")

    # add new line at end of each item
    for item in data:
        f.write(item + "\n")

    # close file
    f.close()

else:
    print("Oops!")
