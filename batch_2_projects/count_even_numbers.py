# Initialize a counter for the even numbers
even_count = 0
# Loop 10 times to get the inputs
for i in range(10):
    user_input = int(input(f"Enter number {i + 1}: "))

    # Check if the number is divisible by 2 with no remainder
    if user_input % 2 == 0:
        even_count += 1

# Print the final count
print(f"Total count of even numbers: {even_count}")