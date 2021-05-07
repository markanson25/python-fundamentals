'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
unique_values = []
while len(unique_values) < 10:
    user_value = input("Please enter a value: ")
    unique_values.append(user_value)
print(unique_values)
for user_input in unique_values:
    counted_input = unique_values.count(user_input)
    if counted_input != 1:
        unique_values.remove(user_input)
print(unique_values)
