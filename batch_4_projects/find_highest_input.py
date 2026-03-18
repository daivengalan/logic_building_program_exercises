highest_number = None

while True:
    entry = input("Enter a number (non-numeric to stop): ")
    if not entry.replace('.', '', 1).isdigit():
        break

    current_value = float(entry)

    if highest_number is None or current_value > highest_number:
        highest_number = current_value

if highest_number is not None:
    print(f"The highest number entered was: {highest_number}")