seen_numbers = []

while True:
    user_input = input("Enter a number (or any non-numeric key to stop): ")

    # Validation check
    if not user_input.replace('.', '', 1).isdigit():
        break

    current_value = float(user_input)

    if current_value in seen_numbers:
        print("Duplicate")
    else:
        print("Unique")
        seen_numbers.append(current_value)