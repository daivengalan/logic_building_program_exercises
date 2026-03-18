#Ask the user for input
first_input_number = float(input("Enter first number: "))
second_input_number = float(input("Enter second number: "))
#Compare the numbers
if first_input_number > second_input_number:
    print(f"The bigger number is: {first_input_number}")
elif second_input_number > first_input_number:
    print(f"The bigger number is: {second_input_number}")
else:
    print("Both numbers are equal.")