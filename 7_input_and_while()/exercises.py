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

number = input("Give me a number: ")
number = int(number)

if number % 10 == 0:
    print("The number " + str(number) + " is a multiple of 10.")
else:
    print("The number " + str(number) + " is not a multiple of 10.")