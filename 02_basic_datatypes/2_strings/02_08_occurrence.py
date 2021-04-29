'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

# user input sentence
sentence = input("Please enter a sentence: ")
# user input letter
letter = input("Please enter a letter: ")
# position of letter
position = sentence.find(letter)
# print result
print(position)
