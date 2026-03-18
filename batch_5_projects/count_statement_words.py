complete_statement = input("Enter a statement: ")

# split() breaks the string into a list of words based on spaces
word_list = complete_statement.split()
total_words = len(word_list)

print(total_words)