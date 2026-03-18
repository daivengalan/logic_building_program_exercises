text_to_search = input("Enter text: ")
char_to_find = input("Enter character to find: ")

found_index = -1
# Loop backwards from the end
for i in range(len(text_to_search) - 1, -1, -1):
    if text_to_search[i] == char_to_find:
        found_index = i
        break

if found_index != -1:
    print(found_index)
else:
    print("Character not found.")