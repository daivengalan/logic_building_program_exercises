base_string = input("Enter string: ")
total_width = int(input("Enter total width: "))

padding_needed = total_width - len(base_string)
if padding_needed > 0:
    # Add spaces to the beginning
    justified_result = (" " * padding_needed) + base_string
else:
    justified_result = base_string

print(f"'{justified_result}'")