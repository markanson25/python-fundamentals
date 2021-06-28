'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

#  I'm not done with this one yet

max_characters = -1
sentence = input("Please enter a short paragraph: ")
split_sentence = sentence.split()
print(split_sentence)
for character in split_sentence:
    counted = split_sentence.count(character)
    if counted > max_characters:
        max_characters = counted
        word_used_most = character
print(word_used_most, "was used", max_characters, "times.")

