# Display output using rounding for floats only

to_round = [1/1, 1/2, 1/3]
print("***** Number to Round *****")
print(to_round)

print()
print("***** Rounded Numbers *****")

for item in to_round:
    if item.is_integer():
        print("{:.0f}".format(item))
    else:
        print("{:.1f}".format(int(item)))
