class Restaurant():
    """simple model of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant is called " + self.restaurant_name.title())
        print("It is specialized in " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now opened!")


restaurant = Restaurant("Willys", 'Spanish food')
restaurant.describe_restaurant()
restaurant.open_restaurant()