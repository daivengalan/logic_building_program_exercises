# Initialize a counter for the odd numbers
odd_count = 0

# Loop 10 times to get the inputs
for i in range(10):
    user_input = int(input(f"Enter number {i + 1}: "))

    # Check if the number has a remainder of 1 when divided by 2
    if user_input % 2 != 0:
        odd_count += 1

# Print the final count of odd numbers
print(f"Total count of odd numbers: {odd_count}")