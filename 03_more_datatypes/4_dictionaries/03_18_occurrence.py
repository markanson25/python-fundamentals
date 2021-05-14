'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

# Initialize
user_input_list = []
user_input_tuple = ()
user_letter_count = []
my_letter_dictionary = {}

# User input
user_input = input("Please enter a sentence: ")

# Add user_input to user_input_list and remove blanks
for user_input_letter in user_input:
    user_input_list.append(user_input_letter)
    if user_input_letter == ' ':
        user_input_list.remove(' ')

# Add letters from user_input_list to user_input_tuple and count letters in list
for refined_user_input_letter in user_input_list:
    user_input_tuple = tuple(user_input_list)
    letter_count = int(user_input.count(refined_user_input_letter))
    user_letter_count.append(letter_count)

# Add dictionary entries from user_input_tuple and user_letter_count
for dictionary_entries in range(0, len(user_input_tuple)):
    my_letter_dictionary[user_input_tuple[dictionary_entries]] = user_letter_count[dictionary_entries]
print(my_letter_dictionary)
