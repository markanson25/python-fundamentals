'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

sentence = input("Please enter a sentence: ")
cut = sentence.split()
print(cut)
listcount = sentence.count(sentence[0])
print(listcount)
