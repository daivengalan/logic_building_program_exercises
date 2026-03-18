input_text = input("Enter text: ")
uppercase_result = ""

for char in input_text:
    # Lowercase 'a' is 97, 'z' is 122. Subtracting 32 converts it to uppercase.
    if "a" <= char <= "z":
        uppercase_result += chr(ord(char) - 32)
    else:
        uppercase_result += char

print(uppercase_result)