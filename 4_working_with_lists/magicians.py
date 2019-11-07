# magicians = ['David', 'Brock', 'Alice']
# for magician in magicians:
#     print(magician.title() + ", that was an awesome trick.")
#     print("Can't wait for you next trick, " + magician.title() + ".\n")
#
#
# #FORRRRRRRRRRR
# for value in range(1, 5):
#     print(value)

# #using range to make a list of numbers
# numbers = list(range(1, 6))
# print(numbers)
#
# #EVEN NUMBERS between 1 and 10
# even_numbers = list(range(2,11,2))
# print(even_numbers)
#
#squares
# squares = []
# for value in range(1, 11):
#     squares.append(value**2)
#     # square = value**2
#     # squares.append(square)
#
# print("squares: " + str(squares))

# #list comprehension
#
# squares = [value**2 for value in range(1, 11)]
# print(squares)
#
# #Working with a part of lists
# players = ['charles','ronaldo','martina','ebi','eliot']
# print(players[0:3])
# print(players[-3:])
#
# print("\n First three players: ")
# for player in players[:3]:
#     print(player.title())


#copying list
my_foods = ['pizza','szpageti','carbonara']
friend_foods = my_foods[:]
#friend_food = my_foods         that wouldn't work, it would create smth like a pointer

my_foods.append("lasagne")
friend_foods.append("chips")

print("My fav foods are:")
print(my_foods)

print("\nMy friend's fav foods are:")
for item in friend_foods:
    print(item)
