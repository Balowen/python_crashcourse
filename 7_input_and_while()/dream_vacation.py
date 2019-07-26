responses = {}

poll_active = True

while poll_active:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world,"
                  " where would you go? ")

    responses[name] = place

    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat.casefold() == 'no':
        poll_active = False

# polling is complete
for name, place in responses.items():
    print(name.title() + " would like to go to " + place.title())