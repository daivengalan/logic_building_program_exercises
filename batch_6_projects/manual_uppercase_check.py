check_text = input("Enter text: ")
is_all_uppercase = True

for char in check_text:
    # If we find any lowercase letter, the whole thing isn't uppercase
    if "a" <= char <= "z":
        is_all_uppercase = False
        break

print(is_all_uppercase)