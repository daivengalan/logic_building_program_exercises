# Initialize the total sum at zero
total_sum = 0
# Use a loop to ask for 10 numbers
for i in range(10):
    current_number = float(input(f"Enter number {i + 1}: "))
    total_sum += current_number
# Display the final calculated sum
print(f"The total sum of all ten numbers is {total_sum}")