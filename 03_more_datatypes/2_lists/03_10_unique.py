'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
# real_unique_list = []
# unique_values = []
# while len(unique_values) < 10:
#     user_value = input("Please enter a value: ")
#     unique_values.append(user_value)
#     if user_value not in real_unique_list:
#         real_unique_list.append(user_value)
# print(real_unique_list)


unique_values = []
while len(unique_values) < 10:
    user_value = input("Please enter a value: ")
    unique_values.append(user_value)
real_unique_list = tuple(set(unique_values))
print(real_unique_list)
