alien_color = 'blue'
if alien_color == 'green':
    print(f'yes the color of the alien is: {alien_color}, the player has just earned 5 points for shooting the alien.')
elif alien_color == 'blue': 
    print('player has just earned 10 points for shooting the alien.')
elif alien_color == 'red':
    print('player has just earned 15 points for shooting the alien.')
else: 
    print('No output')

names = ['admin']

if not names:  # Check if the list is empty
    print('This list is empty')
else:
    for name in names:
        if name == 'admin':
            print(f'Hello, {name}! This is a special greeting for you.')
        else:
            print(f'Hello, {name}')
