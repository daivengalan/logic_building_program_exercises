# Loop 10 times to get the inputs
for i in range(10):
    user_input = int(input(f"Enter number {i + 1}: "))

    # Check if the number is even
    if user_input % 2 == 0:
        # Instead of counting, we print the number directly
        print(f"{user_input} is an even number.")