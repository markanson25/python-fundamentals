'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
user_input_list = []
print("Let's play Rock, Paper, Scissors!")
print("0 = Scissors, 1 = Rock, 2 = Paper")
user_hand_input = int(input("Enter a number: "))
user_input_list.append(user_hand_input)
def user_hand(hand):
    scissors = user_input_list.count(0)
    rocks = user_input_list.count(1)
    papers = user_input_list.count(2)
    if scissors > rocks and scissors > papers:
        most_picked = 0
    elif rocks > scissors and rocks > papers:
        most_picked = 1
    elif papers > scissors and papers > rocks:
        most_picked = 2
    else:
        most_picked = 1
    return most_picked
user_hand(user_hand_input)

def computer_hand(hand):
    if user_hand(user_hand_input) == 0:
        computer_response = 1
    elif user_hand(user_hand_input) == 1:
        computer_response = 2
    elif user_hand(user_hand_input) == 2:
        computer_response = 0
    else:
        computer_response = 1
    return computer_response
while user_hand_input >= 0 and user_hand_input <= 2:
    user_hand_input = int(input("Enter a number: "))
    user_input_list.append(user_hand_input)
    user_hand(user_hand_input)