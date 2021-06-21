'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

word_list = []

with open("words.txt", "r") as words:
    for word in words.readlines():
        word = word.strip()
        split = " - "
        word = word.split(split, 1)[0]
        word = word.capitalize()
        word_list.append(word)

word_list.sort(reverse=True)

with open("reverse_words.txt", "w") as reverse_words:
    reverse_words.write(", \n".join(word_list))

with open("C:/Users/mark_/OneDrive/Documents/CodingNomads/Labs/08_file_io/reverse_words.txt", "r") as reverse_words:
    print(reverse_words.readlines())
