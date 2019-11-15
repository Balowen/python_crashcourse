class Restaurant():
    """simple model of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant is called " + self.restaurant_name.title())
        print("It is specialized in " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now opened!")

    def set_number_served(self,new_number):
        self.number_served = new_number

    def increment_number_served(self, inc_number):
        self.number_served += inc_number


class IceCreamStand(Restaurant):
    """Attempt to model an Ice Cream stand"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'peanut', 'strawberry']

    def get_flavors(self):
        print("The stand has this flavors:")
        for flavor in self.flavors:
            print("\t-" + flavor)


ice_cream_stand = IceCreamStand('PinakoLodo', 'ice creams')
ice_cream_stand.describe_restaurant()
ice_cream_stand.get_flavors()
