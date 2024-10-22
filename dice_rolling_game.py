import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        print(f'({random.randint(1, 6)}, {random.randint(1, 6)})')
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')