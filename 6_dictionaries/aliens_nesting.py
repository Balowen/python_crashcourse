#empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green',
                 'points': 5,
                 'speed': 'slow'
                 }
    aliens.append(new_alien)

# Show the first 4 aliens
for alien in aliens[:4]:
    print(alien)
print("...")

#Show how many aliens were created.
print("Total number of aliens is " + str(len(aliens)))