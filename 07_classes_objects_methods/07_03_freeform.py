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

class Initialize_data():

    def __init__(self):
        self.event_dictionary = {
                                    10001: 'Mental Health - Early Warning Signs and Suicide Prevention',
                                    10002: 'Strategies to Support Multilingual Learners ',
                                    10003: 'Differentiation Strategies',
                                    10004: 'Teaching Reading'
                                 }
        self.event_fee = {10001: 15, 10002: 35, 10003: 25, 10004: 10}
        self.participants = {20001: 'Julie Benson', 20002: 'Andrea Mortensen', 20003: 'Rachel Johnson'}
        self.participant_event_attendance = {
                                                20001: [10001, 10002, 10003],
                                                20002: [10001, 10002, 10003, 10004],
                                                20003: [10001, 10002]
                                            }
        self.current_user = 0

class Gather_user_info(Initialize_data):

    def start_program(self):
        print(f"Hello, {self.user_name_input()}! You are participant number: {self.lookup_name_dictionary_key()}."
              f"  {self.user_event_input()} is event '{self.lookup_event_dictionary_key()}'.!"
              f"  Your total fee is {self.user_event_fee_lookup()}.")

    def __init__(self):
        super().__init__()
        self.start_program()

    def user_name_input(self):
        self.participant_name = input("What is your name?: ")
        if self.participant_name not in self.participants.values():
            new_participant_key = max(self.participants.keys()) + 1
            new_participant_dict_entry = {new_participant_key: self.participant_name}
            self.participants.update(new_participant_dict_entry)
            self.current_user = new_participant_key
        return self.participant_name

    def user_event_input(self):
        self.event_name = input("What event did you attend?: ")
        if self.event_name not in self.event_dictionary.values():
            while self.event_name not in self.event_dictionary.values():
                self.event_name = input("Sorry, that event was not in our system.  Please enter another event: ")
        return self.event_name

    def lookup_event_dictionary_key(self):
        self.user_dictionary_key = 0
        for dictionary_key, dictionary_value in self.event_dictionary.items():
            if self.event_name == dictionary_value:
                self.user_dictionary_key = dictionary_key
        return self.user_dictionary_key

    def lookup_name_dictionary_key(self):
        self.user_name_dictionary_key = 0
        for dictionary_key, dictionary_value in self.participants.items():
            if self.participant_name == dictionary_value:
                self.user_name_dictionary_key = dictionary_key
        return self.user_name_dictionary_key

    def update_participant_event_attendance(self):
        if self.user_name_dictionary_key not in self.participant_event_attendance.keys():
            new_participant_in_event = {self.user_name_dictionary_key: [self.user_dictionary_key]}
            self.participant_event_attendance.update(new_participant_in_event)
        self.user_event_fee_lookup()

    def user_event_fee_lookup(self):
        user_event_name_list = []
        self.total = 0
        user_dictionary_key = min(self.participants)
        if user_dictionary_key != self.user_name_dictionary_key:
            while user_dictionary_key in self.participant_event_attendance.keys() != self.user_name_dictionary_key:
                user_dictionary_key += 1
        elif user_dictionary_key == self.user_name_dictionary_key:
            for user_dict_key, user_dict_values in self.participant_event_attendance.items():
                if user_dict_key == self.user_name_dictionary_key:
                    user_events = user_dict_values
                    for event_key in user_events:
                        for event_fee_key, event_fee in self.event_fee.items():
                            if event_fee_key == event_key:
                                self.total += event_fee
        return self.total


def main():
    user_event = Gather_user_info()
if __name__=="__main__":
    main()
