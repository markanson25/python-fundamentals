'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

word_list = []

with open("words.txt", 'r') as words:
    for word in words.readlines():
        word = word.strip()
        split = " - "
        word = word.split(split, 1)[0]
        word = word.capitalize()
        if len(word) > 1:
            word_list.append(word)

max_length = 0
min_length = 20
word_count = 0
longest_word = ''
smallest_word = ''
for word in word_list:
    word_length = len(word)
    if word_length > max_length:
        max_length = word_length
        longest_word = word
    if word_length < min_length:
        min_length = word_length
        smallest_word = word
    word_count += 1

print(f"The smallest word in the words.txt file is '{smallest_word}', the largest word is '{longest_word}', and the file \n"
      f"contains a total of {word_count} words.")

