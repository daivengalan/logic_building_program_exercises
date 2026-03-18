# Ask the user for two numbers with descriptive variable names
dividend_number = float(input("Enter the first number (dividend): "))
divisor_number = float(input("Enter the second number (divisor): "))
# Perform floor division to remove the decimal point
integer_quotient = int(dividend_number // divisor_number)
# Print the final result
print(f"The quotient without the decimal point is {integer_quotient}")