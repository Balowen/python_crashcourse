#7_1 rental car
# car = input("What car would you like to rent? ")
#
# print("Let me see if I have a " + car + ".")

#7-2 restaurant seating

# group_size = input("How many people are in your dinner group? ")
# group_size = int(group_size)
#
# if group_size > 8:
#     print("You have to wait for a table.")
# else:
#     print("Table is ready.")

#7_3 multiples of ten

# number = input("Give me a number: ")
# number = int(number)
#
# if number % 10 == 0:
#     print("The number " + str(number) + " is a multiple of 10.")
# else:
#     print("The number " + str(number) + " is not a multiple of 10.")

#7_4 pizza toppings
# prompt = "Enter a pizza topping: "
# prompt += "\n(Type 'quit' to close the program.) "
#
# while True:
#     topping = input(prompt)
#
#     if topping == 'quit':
#         break
#     else:
#         print("I'll add " + topping + " to your pizza.")

#7-5 movie tickets
prompt = "Enter your age: "
prompt += "\n(Type 'quit' to close the program.) "

active = True
while active:
    age = input(prompt)

    if age == 'quit':
        active = False
        break

    age = int(age)

    if age <= 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
