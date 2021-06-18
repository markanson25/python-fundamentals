'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

word_list = []
with open("words.txt", "r") as words:
    for word in words.readlines():
        word = word.rstrip()
        word = word.lstrip()
        sep = ' - '
        word = word.split(sep, 1)[0]
        word = word.capitalize()
        if len(word) > 10:
            word_list.append(word)
print(word_list)

