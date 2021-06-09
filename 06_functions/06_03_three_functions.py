'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

user_input_list = []
user_hand_input = 1

print("Let's play Rock, Paper, Scissors!")
print("0 = Scissors, 1 = Rock, 2 = Paper, 3 = Exit")

while user_hand_input >= 0 and user_hand_input <= 2:
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

    def computer_hand(most_picked):
        if most_picked == 0:
            computer_response = 1
        elif most_picked == 1:
            computer_response = 2
        elif most_picked == 2:
            computer_response = 0
        else:
            computer_response = 1
        return computer_response

    def game_functions(user_input, computer_response):
        if user_hand_input == 0:
            user_choice = "Scissors"
        elif user_hand_input == 1:
            user_choice = "Rock"
        elif user_hand_input == 2:
            user_choice = "Paper"
        if computer_response == 0:
            computer_choice = "Scissors"
        elif computer_response == 1:
            computer_choice = "Rock"
        elif computer_response == 2:
            computer_choice = "Paper"
        if user_hand_input == 0 and computer_response == 2:
            outcome = "You win!"
        elif user_hand_input == 0 and computer_response == 0:
            outcome = "Tie!  Try again!"
        elif user_hand_input == 0 and computer_response == 1:
            outcome = "You lose!"
        if user_hand_input == 1 and computer_response == 0:
            outcome = "You win!"
        elif user_hand_input == 1 and computer_response == 1:
            outcome = "Tie!  Try again!"
        elif user_hand_input == 1 and computer_response == 2:
            outcome = "You lose!"
        if user_hand_input == 2 and computer_response == 1:
            outcome = "You win!"
        elif user_hand_input == 2 and computer_response == 2:
            outcome = "Tie!  Try again!"
        elif user_hand_input == 2 and computer_response == 0:
            outcome = "You lose!"
        return print(f"{outcome}  You picked {user_choice}, the computer picked {computer_choice}")
    game_output = game_functions(user_hand_input, computer_hand(user_hand(user_hand_input)))