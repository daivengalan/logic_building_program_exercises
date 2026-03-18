input_list = []
duplicates_found = []

for i in range(10):
    user_input = float(input(f"Enter number {i + 1}: "))
    input_list.append(user_input)

for current_number in input_list:
    # If the number appears more than once and isn't already in our 'found' list
    if input_list.count(current_number) > 1 and current_number not in duplicates_found:
        duplicates_found.append(current_number)

print("Numbers that have duplicates:")
for duplicate in duplicates_found:
    print(duplicate)