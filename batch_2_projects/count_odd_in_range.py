# Initialize a counter for the specific odd numbers we want
odd_count_in_range = 0

# Loop 10 times to get the inputs
for i in range(10):
    user_input = int(input(f"Enter number {i + 1}: "))

    # Check if the number is between 1 and 100 AND is odd
    if 1 <= user_input <= 100 and user_input % 2 != 0:
        odd_count_in_range += 1

# Display the final count of numbers that fit both criteria
print(f"Total count of odd numbers between 1 and 100: {odd_count_in_range}")