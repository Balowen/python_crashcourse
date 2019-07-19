favorite_languages = {
    'jen': ['python', 'go'],
    'sarah': ['c++'],
    'eddie': ['ruby', 'haskell'],
    'phil': ['python'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(name.title() + "'s favorite language is ")
    else:
        print(name.title() + "'s favorite language are:")

    for language in languages:
        print('\t' + language.title())
