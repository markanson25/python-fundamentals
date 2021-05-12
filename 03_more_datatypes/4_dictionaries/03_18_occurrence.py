'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

user_input_list = []
user_input_tuple = ()
user_letter_count = []

user_input = input("Please enter a sentence: ")

for user_input_letter in user_input:
    user_input_list.append(user_input_letter)
    # if user_input_letter == ' ':
    #     user_input_list.remove(' ')
    user_input_tuple = tuple(user_input_list)
    letter_count = user_input_list.count(user_input_letter)
    user_letter_count.append(letter_count)
    # if letter_count == 0:
    #     user_letter_count.remove(0)

print(user_input_list)
print(user_input_tuple)
print(user_letter_count)
