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



class Gather_course_and_participant_info():

    def __init__(self):
        self.event_name = input("What event did you attend?: ")
        self.event_name_list = []
        self.event_name_list.append(self.event_name)

    def store_user_input(self):
        pass

    def __str__(self):
        return f"{self.event_name} was added to the list {self.event_name_list}!"

class License_renewal_courses:

    def __init__(self, event_name, date, delivery):
        self.event_name = event_name
        self.date = date
        self.delivery = delivery

    def __str__(self):
        return f"The License Renewal training '{self.event_name}' took place {self.date} and was delivered {self.delivery}."

class Participants:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return f" "

user_event = Gather_course_and_participant_info()
print(user_event.__str__())


# my_event = License_renewal_courses('Differention Strategies', '05/30/2021', 'On Demand')
# my_participation = Participants('Mark', 'Anson', 'mark_anson@yahoo.com')
# my_presenter = Presenter('Jacki Brickman', 'Yes', 2500)
#
# print(my_event.__str__(), my_participation.__str__(), my_presenter.__str__())