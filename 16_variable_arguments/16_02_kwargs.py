'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def course_fees(**kwargs):
    aggregate_fees = 0
    events_list = []
    for event, fee in kwargs.items():
        adding_fees = fee + aggregate_fees
        events_list.append(event)
        aggregate_fees += fee
    print(f"Thank you for attending {events_list}!  The total price for the events is: {adding_fees}")

course_fees(Reading=100, Math=150, History=75)
