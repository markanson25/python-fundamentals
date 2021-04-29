'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

# User Input for sentence
sentence = input("Type a sentence and hit enter: ")
# User input for symbol
symbol = input("Type a symbol and hit enter: ")
# Assign variable to the first character
first_character = sentence[:1]
# replace with symbol
output = sentence.replace(first_character, symbol)
# print result
print(output)
