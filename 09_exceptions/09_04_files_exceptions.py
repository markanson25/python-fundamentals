'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character of each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

UnicodeDecodeError
'''
counter = 0
error_free = False
text_files_list = []
first_characters_list = []
war_and_peace = []
pride_and_prejudice = []
crime_and_punishment = []

class Prince(Exception):

    def print_exception(self):
        return f"Can you believe that the word 'Prince' was used within the first 100 words of this text!?!?"

with open("Books/war_and_peace.txt", "r", errors='ignore') as war_and_peace_text:
    for word in war_and_peace_text.readlines():
        word = word.strip()
        word = word.replace(',','')
        word = word.split(' ')
        war_and_peace.append(word)
    text_files_list.append(war_and_peace)
with open("Books/pride_and_prejudice.txt", "r", errors='ignore') as pride_and_prejudice_text:
    for word in pride_and_prejudice_text.readlines():
        word = word.strip()
        word = word.replace(',','')
        word = word.split(' ')
        pride_and_prejudice.append(word)
    text_files_list.append(pride_and_prejudice)
with open("Books/crime_and_punishment.txt", "w", errors='ignore') as crime_and_punishment_text:
    crime_and_punishment_text.write('')
with open("Books/crime_and_punishment.txt", "r", errors='ignore') as crime_and_punishment_text:
    for word in crime_and_punishment_text.readlines():
        word = word.strip()
        word = word.replace(',','')
        word = word.split(' ')
        crime_and_punishment.append(word)
    text_files_list.append(crime_and_punishment)

while error_free == False:
    try:
        first_file = first_characters_list.append(text_files_list[0][0])
    except IndexError as error:
        first_file = first_characters_list.append('null')
    try:
        second_file = first_characters_list.append(text_files_list[1][0])
    except IndexError as error:
        second_file = first_characters_list.append('null')
    try:
        third_file = first_characters_list.append(text_files_list[2][0])
    except IndexError as error:
        third_file = first_characters_list.append('null')
    error_free = True

print(first_characters_list)

while counter < 100:
    for file in text_files_list:
        for file_list in file:
            for word in file_list:
                if word == "Prince":
                    raise Prince()
            counter += 1
