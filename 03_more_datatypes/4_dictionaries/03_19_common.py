'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

# Initialize
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}
dict_3 = {}
key_set = list(dict_1.keys()) + list(dict_2.keys())
data_type = type(key_set)
key_set = set(key_set)
# print(key_set)
for key_letter in key_set:
    if key_letter in dict_1.keys() and key_letter in dict_2.keys():
        value_addition = dict_1[key_letter] + dict_2[key_letter]
        dict_3[key_letter] = value_addition
    elif key_letter in dict_1.keys():
        dict_3[key_letter] = dict_1[key_letter]
    elif key_letter in dict_2.keys():
        dict_3[key_letter] = dict_2[key_letter]
print(dict_3)
# for key, value in dict_3.items():
#     if key in dict_1 and key in dict_2:
#         dict_3.values()
# print(dict_3)

