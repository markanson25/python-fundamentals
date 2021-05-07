'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

#  I'm not done with this one yet

max_characters = -1
sentence = input("Please enter a short paragraph: ")
cut = sentence.split()
for character in cut:
    counted = cut.count(character)
    if counted > max_characters:
        max_characters = counted
        print(character, "was used", max_characters, "times.")

