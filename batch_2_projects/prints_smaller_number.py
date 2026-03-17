#Ask the user for input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
#Compare the numbers
if num1 < num2:
    print(f"The smaller number is: {num1}")
elif num2 < num1:
    print(f"The smaller number is: {num2}")
else:
    print("Both numbers are equal.")