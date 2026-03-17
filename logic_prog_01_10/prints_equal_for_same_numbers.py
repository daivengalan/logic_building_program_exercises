#Ask the user for two numbers
first_input_number = float(input("Enter the first number: "))
second_input_number = float(input("Enter the second number: "))
#Compare and prints the bigger number using an if-else statement
if first_input_number > second_input_number:
    print(f"The bigger number is: {first_input_number}")
elif second_input_number > first_input_number:
    print(f"The bigger number is: {second_input_number}")
#For if the numbers are exactly the same
else:
    print("Equal")
