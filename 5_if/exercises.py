colors = ('yellow', 'green', 'red')
alien_color = colors[2]

if alien_color.lower() == 'green':
    print("You earn 5 points")
elif alien_color.lower() == 'yellow':
    print("You earn 10 points")
elif alien_color.lower() == 'red':
    print("You earn 15 points")

#5_7 favourite fruit
print('\n')

favorite_fruits = ['banana', 'apple', 'strawberry']

if 'banana' in favorite_fruits:
    print("You really like bananas")
if 'apple' in favorite_fruits:
    print("You really like apples")
if 'strawberry' in favorite_fruits:
    print("You really like strawberrys")
if 'onion' in favorite_fruits:
    print("Onion is not a fruit and you stink")