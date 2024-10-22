import random

words = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
choice = ('r', 'p', 's')

while True:
    user_choice = input('Rock, Paper, Scissors? (r/p/s): ').lower()
    if user_choice not in choice:
        print('invalid choice!')
        continue

    computer_choice = random.choice(choice)

    print(f'You chose {words[user_choice]}!')
    print(f'Computer chose {words[computer_choice]}!')

    if user_choice == computer_choice:
        print('Tie!')
    elif ((user_choice == 'r' and computer_choice == 's') or
          (user_choice == 'p' and computer_choice == 'r') or
          (user_choice == 's' and computer_choice == 'p')):
        print('You win!')
    else:
        print('You lose')

    play_again = input('Continue? (y/n): ').lower()
    if play_again == 'n':
        break
