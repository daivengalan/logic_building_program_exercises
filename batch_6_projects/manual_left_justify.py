base_string = input("Enter string: ")
total_width = int(input("Enter total width: "))

padding_needed = total_width - len(base_string)
# If padding is positive, add spaces to the end
if padding_needed > 0:
    justified_result = base_string + (" " * padding_needed)
else:
    justified_result = base_string

print(f"'{justified_result}'")