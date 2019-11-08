# Sandwiches

def make_sandwich(*items):
    print("Making a sandwich with:")
    for item in items:
        print("- " + item)


make_sandwich("salami")
make_sandwich("salami",'ser', 'ogorek')