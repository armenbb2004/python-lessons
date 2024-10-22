import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
words = {ROCK: 'rock', PAPER: 'paper', SCISSORS: 'scissors'}
choice = tuple(words.keys())


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
    elif ((user_choice == ROCK and computer_choice == SCISSORS) or
          (user_choice == PAPER and computer_choice == ROCK) or
          (user_choice == SCISSORS and computer_choice == PAPER)):
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
