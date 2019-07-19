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
}

for word, meaning in glossary.items():
    print(word + "\n\t" + meaning)