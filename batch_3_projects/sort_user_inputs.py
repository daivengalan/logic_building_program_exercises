collected_numbers = []

while True:
    user_input = input("Enter a number (non-numeric to stop): ")

    if not user_input.replace('.', '', 1).isdigit():
        break

    collected_numbers.append(float(user_input))

# Using the sort() function as suggested
collected_numbers.sort()

print("Numbers from lowest to highest:")
for sorted_value in collected_numbers:
    print(sorted_value)