favorite_languages = {
    'jen': ['python', 'go'],
    'sarah': ['c++'],
    'eddie': ['ruby', 'haskell'],
    'phil': ['python'],
}

friends = ['phil', 'sarah']

# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")

# looping through all the keys in dictionary

#without keys() is the same thing
# for name in favorite_languages:
#     print(name.title())

for name in sorted(favorite_languages.keys()):
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll.")

print("\nThe following languages have been mentioned:")
#set() makes a set of unique languages
for language in set(favorite_languages.values()):
    print(language.title())

