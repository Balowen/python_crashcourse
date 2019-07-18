available_toppings = ('mushrooms', 'ketchup', 'pineapple',
                      'onions', 'cheese', 'olives')

requested_toppings = ['mushrooms', 'ketchup',
                      'onions', 'cheese']
# requested_toppings = []

# if requested_toppings != 'anchovies':
#     print("Hold the anchovies!")
#
# if 'cheese' in requested_toppings:
#     print("Adding cheese")
# if 'onions' in requested_toppings:
#     print("Adding extra onions")
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print("Adding " + requested_topping + ".")
        else:
            print("Sorry, we don't have " + requested_topping + '.')
else:
    print("Are you sure you want a plain pizza?")