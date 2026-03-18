messy_string = input("Enter text: ")
words_list = messy_string.split()
capitalized_words = []

for word in words_list:
    # Manual capitalize logic for each word
    if len(word) > 0:
        first = word[0]
        if "a" <= first <= "z":
            first = chr(ord(first) - 32)

        rest = ""
        for char in word[1:]:
            if "A" <= char <= "Z":
                rest += chr(ord(char) + 32)
            else:
                rest += char
        capitalized_words.append(first + rest)

print(" ".join(capitalized_words))