input_history = []
unique_entries = []

for i in range(10):
    user_input = float(input(f"Enter number {i + 1}: "))
    input_history.append(user_input)

for current_number in input_history:
    if current_number not in unique_entries:
        unique_entries.append(current_number)

print("Displaying numbers (duplicates excluded):")
for unique_number in unique_entries:
    print(unique_number)