import random

words = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
choice = ('r', 'p', 's')


def get_user_choice():
    while True:
        user_choice = input('Rock, Paper, Scissors? (r/p/s): ').lower()
        if user_choice in choice:
            return user_choice
        else:
            print('invalid choice!')


def display_choices(user_choice, computer_choice):
    print(f'You chose {words[user_choice]}!')
    print(f'Computer chose {words[computer_choice]}!')


def determinate_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif ((user_choice == 'r' and computer_choice == 's') or
          (user_choice == 'p' and computer_choice == 'r') or
          (user_choice == 's' and computer_choice == 'p')):
        print('You win!')
    else:
        print('You lose')


def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choice)

        display_choices(user_choice, computer_choice)

        determinate_winner(user_choice, computer_choice)

        play_again = input('Continue? (y/n): ').lower()
        if play_again == 'n':
            break


play_game()
