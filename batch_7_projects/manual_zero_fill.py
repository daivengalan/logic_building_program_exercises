numeric_string = input("Enter a numeric string: ")
target_length = int(input("Enter target length: "))

zeros_to_add = target_length - len(numeric_string)
if zeros_to_add > 0:
    filled_result = ("0" * zeros_to_add) + numeric_string
else:
    filled_result = numeric_string

print(filled_result)