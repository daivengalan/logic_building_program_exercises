search_text = input("Enter the full text: ")
target_char = input("Enter the character to count: ")

occurrence_count = 0
for char in search_text:
    if char == target_char:
        occurrence_count += 1

print(occurrence_count)