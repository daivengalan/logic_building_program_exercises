number_list = []

for i in range(10):
    user_input = float(input(f"Enter number {i + 1}: "))
    number_list.append(user_input)

print("Numbers without any duplicates:")
for current_number in number_list:
    # count() tells us how many times the number appears in the list
    if number_list.count(current_number) == 1:
        print(current_number)