#empty list for storing aliens
aliens = []

# Make 30 green aliens; each alien is a dictionary
for alien_number in range(30):
    new_alien = {'color': 'green',
                 'points': 5,
                 'speed': 'slow'
                 }
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...\n")

#Show how many aliens were created.
print("Total number of aliens is " + str(len(aliens)))