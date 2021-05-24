'''
Using f-strings, print out the name, last name, and favorite
office supply item of each person in the given dictionary,
formatted like so:

LASTNAME, Name           Office supply item
LONGERLASTNAME, Name     Office supply item

'''

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]
# This is my original code and didn't want to mess up playing around.

# quote_selection = 0
# for quote_selection in range(len(office)):
#     quote_selection_name = office[quote_selection]["full_name"].split()
#     # quote_selection_item = office[quote_selection]["item"]
#     # print(f"{quote_selection_name[1]}, {quote_selection_name[0]: <10} {quote_selection_item}")
#     quote_selection_last_name_length = len(quote_selection_name[1])
#     dictionary_update_info = {"Last_Name_Length": quote_selection_last_name_length}
#     office[quote_selection].update(dictionary_update_info)
#     print(office)

#  This is the code I am playing around with, generally the same as above with some changes

last_name_length_list = []
quote_selection = 0
for quote_selection in range(len(office)):  # Iterate through the list
    quote_selection_name = office[quote_selection]["full_name"].split()  # Break first and last names apart
    # quote_selection_item = office[quote_selection]["item"]  # Get the office item for each person
    # print(f"{quote_selection_name[1]}, {quote_selection_name[0]: <10} {quote_selection_item}")  #  My f string showing my results
    quote_selection_last_name_length = len(quote_selection_name[1])  # Get length of last name
    last_name_length_list.append(quote_selection_last_name_length)  #  Append length of last name to list for sorting
    dictionary_update_info = {"Last_Name_Length": quote_selection_last_name_length}  # Add length to dictionary (I hoped to sort with this)
    office[quote_selection].update(dictionary_update_info)  # Update dictionary with last name length
    last_name_length_list.sort(reverse=True)  # Sorting the list of last name lengths descending
print(last_name_length_list)
print(office[0].get('Last_Name_Length'))
