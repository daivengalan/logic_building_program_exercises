original_casing = input("Enter text: ")
swapped_result = ""

for char in original_casing:
    if "A" <= char <= "Z":
        swapped_result += chr(ord(char) + 32)
    elif "a" <= char <= "z":
        swapped_result += chr(ord(char) - 32)
    else:
        swapped_result += char

print(swapped_result)