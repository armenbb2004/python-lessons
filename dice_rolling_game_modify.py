import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        roll_count = int(input('Select roll count: '))
        count = 0;
        while roll_count > count:
            count += 1
            print(f'({random.randint(1, 6)}, {random.randint(1, 6)})')
        print(f'You rolled {count} times.')
        break
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')