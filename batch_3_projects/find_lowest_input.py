lowest_number = None

while True:
    user_entry = input("Enter a number (non-numeric to stop): ")

    if not user_entry.replace('.', '', 1).isdigit():
        break

    current_number = float(user_entry)

    # Initialize or update the lowest number
    if lowest_number is None or current_number < lowest_number:
        lowest_number = current_number

if lowest_number is not None:
    print(f"The lowest number entered was: {lowest_number}")