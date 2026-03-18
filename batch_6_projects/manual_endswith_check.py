main_string = input("Enter the main string: ")
suffix_to_find = input("Enter the ending to check: ")

# Compare the end of the main string to the suffix
if main_string[-len(suffix_to_find):] == suffix_to_find:
    print(True)
else:
    print(False)