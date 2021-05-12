'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

user_input_key_list = []
user_input_value_list = []
user_input_key_tuple = ()
user_input_value_tuple = ()
my_dictionary = {}

while len(user_input_key_list) < 10:
    user_input = int(input("Please enter a number: "))
    user_input_key_list.append(user_input)
    user_input_key_tuple = tuple(user_input_key_list)
    user_input_multiplication = user_input ** 2
    user_input_value_list.append(user_input_multiplication)
    user_input_value_tuple = tuple(user_input_value_list)

for dictionary_entry in range(0, len(user_input_key_tuple)):
    my_dictionary[user_input_key_tuple[dictionary_entry]] = user_input_value_tuple[dictionary_entry]
print(my_dictionary)
