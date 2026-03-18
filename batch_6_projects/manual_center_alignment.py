text_to_center = input("Enter text: ")
target_width = int(input("Enter total width: "))

padding_total = target_width - len(text_to_center)
if padding_total > 0:
    left_padding = padding_total // 2
    right_padding = padding_total - left_padding
    centered_text = (" " * left_padding) + text_to_center + (" " * right_padding)
else:
    centered_text = text_to_center

print(f"'{centered_text}'")
