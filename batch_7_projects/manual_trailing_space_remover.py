user_input_string = input("Enter a string with trailing spaces: ")

end_index = len(user_input_string) - 1
# Work backwards from the end until we hit a non-space character
while end_index >= 0 and user_input_string[end_index] == " ":
    end_index -= 1

# Slice from the beginning up to the last non-space character 
cleaned_string = user_input_string[:end_index + 1]
print(f"'{cleaned_string}'")