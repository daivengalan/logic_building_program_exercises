text_to_search = input("Enter text: ")
char_to_find = input("Enter character to find: ")

found_index = -1
# 'i' is allowed as a loop counter
for i in range(len(text_to_search)):
    if text_to_search[i] == char_to_find:
        found_index = i
        break

if found_index != -1:
    print(found_index)
else:
    print("Character not found.")