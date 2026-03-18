user_input_string = input("Enter a string with leading spaces: ")

start_index = 0
# Find the first character that isn't a space
while start_index < len(user_input_string) and user_input_string[start_index] == " ":
    start_index += 1

# Slice the string from that point to the end
cleaned_string = user_input_string[start_index:]
print(cleaned_string)