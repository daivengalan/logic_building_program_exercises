main_text = input("Enter the full text: ")
suffix_to_remove = input("Enter the suffix to remove: ")

suffix_length = len(suffix_to_remove)

# Check if the end of the text matches the suffix
if main_text[-suffix_length:] == suffix_to_remove:
    result_text = main_text[:-suffix_length]
else:
    result_text = main_text

print(result_text)