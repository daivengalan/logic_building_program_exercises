input_text = input("Enter text: ")
lowercase_result = ""

for character in input_text:
    # ASCII 'A' is 65, 'Z' is 90. Adding 32 converts it to lowercase.
    if "A" <= character <= "Z":
        lowercase_result += chr(ord(character) + 32)
    else:
        lowercase_result += character

print(lowercase_result)