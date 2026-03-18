raw_name_input = input("Enter your name: ")

# Lowercase everything and replace spaces with underscores
snake_case_output = raw_name_input.lower().replace(" ", "_")

print(snake_case_output)