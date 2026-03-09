# Initialize the total sum and the counter
total_sum = 0.0
counter = 0
# Using a while loop to ask for 10 numbers
while counter < 10:
    # Adding 1 to the display so the user sees "Number 1", "Number 2", etc.
    user_input = float(input(f"Enter number {counter + 1}: "))
    # Add the input to our running total
    total_sum += user_input
    # Increment the counter 
    counter += 1
#Print the sum of 10 num
print(f"The total sum of the 10 numbers is: {total_sum}")