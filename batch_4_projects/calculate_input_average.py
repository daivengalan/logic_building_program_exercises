total_sum = 0
entry_count = 0

while True:
    entry = input("Enter a number (non-numeric to stop): ")
    if not entry.replace('.', '', 1).isdigit():
        break

    total_sum += float(entry)
    entry_count += 1

if entry_count > 0:
    average_result = total_sum / entry_count
    print(f"The average of all entered numbers is: {average_result}")
else:
    print("No numbers were entered.")