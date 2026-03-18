# Ask the user for the boundary numbers with descriptive names
starting_number = int(input("Enter the starting number: "))
ending_number = int(input("Enter the ending number: "))
# We add + 1 to ending_number so the second number is included in the print
for i in range(starting_number, ending_number + 1):
    print(i)