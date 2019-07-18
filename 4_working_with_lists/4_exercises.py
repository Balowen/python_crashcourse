#EXERCISES
print("exercises\n")
#4.1
pizzas = ['arabska', 'pepperoni', 'mrozona']
for pizza in pizzas:
    print("I like " + pizza + " pizza")

print('DAAAAAMN I love pizza\n')

#4.2
animals = ['cat', 'dog', 'elephant']
for animal in animals:
    print(animal.title() + " would make a great pet")
print("I would love to get any of those\n")



#4-3
for value in range(1,21):
    print(value)

#4-4
# million_numbers = list(range(1,1000001))
# for number in million_numbers:
#     print(number)

#4-5
numbers = list(range(1,1000001))
print("min = " + str(min(numbers))+ "\t\tmax = " + str(max(numbers)))
print("sum = " + str(sum(numbers)))

#4-6 odd numbers
odd_numbers = list(range(1,21,2))
for number in odd_numbers:
    print(number)

#4-7 threes
threes = list(range(3,31,3))
for number in threes:
    print(number)

#4-8 cubes
cubes_list = []
for value in range(1,11):
    cubes_list.append(value**3)
print(cubes_list)

#4-9
cubes_list = [value**3 for value in range(1,11)]
print(cubes_list)

#4_10
animals = ['cat', 'dog', 'elephant','cockroach','dingo']
print("The first three animals in the list are:")
print(animals[0:3])

print("Three items from the middle of the list are:")
print(animals[1:4])

print("the last three items:")
print(animals[-3:])

#4-11
my_pizzas = ['arabska', 'pepperoni', 'mrozona']
friend_pizzas = my_pizzas[:]

my_pizzas.append('calzone')
friend_pizzas.append('roma')

print("My favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("My friend fav pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
print('DAAAAAMN I love pizza\n')