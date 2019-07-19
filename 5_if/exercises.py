colors = ('yellow', 'green', 'red')
alien_color = colors[2]

if alien_color.lower() == 'green':
    print("You earn 5 points")
elif alien_color.lower() == 'yellow':
    print("You earn 10 points")
elif alien_color.lower() == 'red':
    print("You earn 15 points")

# 5_7 favourite fruit
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

print("\n")
# 5_8 hello admin
users = ['derek', 'hakero', 'admin', 'kali', 'zupa']

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again.")
else:
    print("We need to find some users!")

# 5_10 checking usernames
print('\n')

current_users = ['derek', 'hakero', 'kanoli', 'KALI', 'zupa']
new_users = ['kali', 'zupa', 'baku', 'granola']


for user in new_users:
    if user.lower() in current_users:
        print("Think about different username")
    elif user.title() in current_users:
        print("Think about different username")
    elif user.upper() in current_users:
        print("Think about different username")
    else:
        print("U'r cool")

#5_11
print("\n")
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
