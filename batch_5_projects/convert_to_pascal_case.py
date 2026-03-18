raw_name_input = input("Enter your name: ")

# Fix casing, split into words, then join with no spaces
words = raw_name_input.title().split()
pascal_case_output = "".join(words)

print(pascal_case_output)