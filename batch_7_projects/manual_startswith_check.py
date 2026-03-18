main_string = input("Enter the main string: ")
prefix_to_find = input("Enter the beginning to check: ")

# Compare the start of the main string to the prefix length
if main_string[:len(prefix_to_find)] == prefix_to_find:
    print(True)
else:
    print(False)