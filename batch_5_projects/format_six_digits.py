user_number = int(input("Enter a number (0-1000): "))

# zfill pads the string with zeros at the beginning
six_digit_format = str(user_number).zfill(6)

print(six_digit_format)