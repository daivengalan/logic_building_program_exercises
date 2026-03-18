raw_input = input("Enter text: ")

if len(raw_input) > 0:
    # First char to upper
    first_char = raw_input[0]
    if "a" <= first_char <= "z":
        first_char = chr(ord(first_char) - 32)

    # Rest to lower
    rest_of_string = ""
    for char in raw_input[1:]:
        if "A" <= char <= "Z":
            rest_of_string += chr(ord(char) + 32)
        else:
            rest_of_string += char

    print(first_char + rest_of_string)
    