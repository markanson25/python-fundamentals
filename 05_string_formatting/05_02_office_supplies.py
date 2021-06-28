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

quote_selection = 0
for quote_selection in range(len(office)):
    quote_selection_name = office[quote_selection]["full_name"].split()
    quote_selection_name_length = len(office[quote_selection]["full_name"])
    quote_selection_item = office[quote_selection]["item"]
    # print(f"{quote_selection_name[1].upper()}, {quote_selection_name[0]} {quote_selection_item: >{40-quote_selection_name_length}}")
    # print(quote_selection_name_length)
    name = f"{quote_selection_name[1].upper()}, {quote_selection_name[0].capitalize()}"
    print(f"{name: <20} {quote_selection_item}")

