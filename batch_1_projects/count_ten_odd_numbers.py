# Initialize a counter to track how many odds we find
odd_number_count = 0

# Loop 10 times to collect user inputs
for i in range(10):
    user_input = int(input(f"Enter number {i + 1}: "))

    # If the remainder is not 0 when divided by 2, it's odd
    if user_input % 2 != 0:
        odd_number_count += 1

# Display the total count
print(f"Total count of odd numbers: {odd_number_count}")