'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''

class License_renewal_courses:

    def __init__(self, event_name, date, delivery):
        self.event_name = event_name
        self.date = date
        self.delivery = delivery

    def __str__(self):
        f"The License Renewal training '{self.event_name}' took place {self.date} and was delivered {self.delivery}."

class Participants:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        f" "

class Presenter:

    def __init__(self, full_name, contract_on_file, fee):
        self.full_name = full_name
        self.contract_on_file = contract_on_file
            if self.contract_on_file == "Yes" or "yes"
                contract_on_file = "is"
            elif self.contract_on_file == "No" or "no"
                contract_on_file = "is not"
        self.fee = fee

    def __str__(self):
        f"{self.full_name} facilitated the event and charged {self.fee}.  The contract {self.contract_on_file} on file."
