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

restaurant = Restaurant("Willys", 'Spanish food')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("This restaurant served " + str(restaurant.number_served) + " clients.")
restaurant.set_number_served(3)
print("This restaurant served " + str(restaurant.number_served) + " clients.")
restaurant.increment_number_served(5)
print("This restaurant served " + str(restaurant.number_served) + " clients.")
