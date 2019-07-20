#6-1 Person
friend = {
    'first_name': 'kamil',
    'last_name': 'król',
    'age': 21,
    'city': 'wrocław',
}

print(friend)
#6-2 favorite numbers
favorite_numbers = {
    'sarah': 5,
    'kamil': 12,
    'justin': 53,
    'ellie': 23,
}

print("Favorite numbers of polled people: " + str(favorite_numbers))
print("\n")
#6-3 Glossary
glossary = {
    'if': 'used to create a condition/check',
    'dictionary': 'key-value based data structure',
    'for': 'used to initiate a for loop',
    'print': 'used to display text',
    'list': 'cool way to store a lot of values of any kind',
    'set()': 'makes a set of unique items from dictionary'
}

for word, meaning in glossary.items():
    print(word + "\n\t" + meaning)

#6-5 rivers
print("\n")

rivers = {
    'nile': 'egypt',
    'wieprz': 'poland',
    'wisla': 'poland',
}

for river, country in rivers.items():
    print("The " + river.title() +
          " runs through " + country.title() + ".")

print("\nMentioned rivers:")
for river in set(rivers.keys()):
    print(river.title())

print("\nMentioned countries:")
for country in set(rivers.values()):
    print(country.title())

#6-6 Pooling
print("\n")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c++',
    'eddie': 'ruby',
    'phil': 'python',
}

people_to_ask = ['phil', 'sarah',
                 'ricky', 'morty']

for name in people_to_ask:
    if name in favorite_languages.keys():
        print("Thanks for responding " + name.title())
    else:
        print(name.title() + ", please take the poll.")

#6-8 people
friend_0 = {
    'first_name': 'kamil',
    'last_name': 'król',
    'age': 21,
    'city': 'wrocław',
    }
friend_1 = {
    'first_name': 'jon',
    'last_name': 'snow',
    'age': 21,
    'city': 'winterfell',
    }
friend_2 = {
    'first_name': 'kali',
    'last_name': 'linux',
    'age': 26,
    'city': 'computerville',
    }

friends = [friend_0, friend_1, friend_2]

for friend in friends:
    full_name = friend['first_name'] + " " + friend['last_name']
    age = str(friend['age'])

    print("\n" + full_name.title() + "\n\tage: " + age +
          "\n\tcity: " + friend['city'].title())

#6-8 pets
reksio = {
    'animal': 'dog',
    'owner': 'bartek'
}
pikus = {
    'animal': 'dog',
    'owner': 'julia'
}
harambe = {
    'animal': 'gorilla',
    'owner': 'zooman'
}

pets = [reksio, pikus, harambe]

for pet in pets:
    print(pet)

#6-9 favorite_places
favorite_places = {
    'bartek': ['rome', 'krasnobród', 'leba'],
    'aneta': ['rome', 'warsaw'],
    'julia': ['leba', 'zamosc'],
}

for name, places in favorite_places.items():
    print(name.title() + "'s favorite places:")
    for place in places:
        print("\t" + place.title())

