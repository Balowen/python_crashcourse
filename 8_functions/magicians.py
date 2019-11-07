

def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians, great_magicians):
    while magicians:
        magician = magicians.pop()
        great_magicians.append(magician + " the Great")



magicians = ['Eduardo', 'Callini', 'Prosciuttini']
great_magicians = []

show_magicians(magicians)
make_great(magicians, great_magicians)
show_magicians(great_magicians)
show_magicians(magicians)
