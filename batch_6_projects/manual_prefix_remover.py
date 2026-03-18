original_text = input("Enter the full text: ")
prefix_to_remove = input("Enter the prefix to remove: ")

# Check if the start of the text matches the prefix
if original_text[:len(prefix_to_remove)] == prefix_to_remove:
    result_text = original_text[len(prefix_to_remove):]
else:
    result_text = original_text

print(result_text)