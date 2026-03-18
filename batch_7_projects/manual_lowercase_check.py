check_text = input("Enter text: ")
is_all_lowercase = True

for char in check_text:
    # If we find any uppercase letter, the whole thing isn't lowercase
    if "A" <= char <= "Z":
        is_all_lowercase = False
        break

print(is_all_lowercase)