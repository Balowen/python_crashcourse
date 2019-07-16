magicians = ['David', 'Brock', 'Alice']
for magician in magicians:
    print(magician.title() + ", that was an awesome trick.")
    print("Can't wait for you next trick, " + magician.title() + ".\n")

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

#FORRRRRRRRRRR
for value in range(1, 5):
    print(value)

#using range to make a list of numbers
numbers = list(range(1, 6))
print(numbers)

#EVEN NUMBERS between 1 and 10
even_numbers = list(range(2,11,2))
print(even_numbers)

#squares
squares = []
for value in range(1,11):
    squares.append(value**2)
    # square = value**2
    # squares.append(square)

print("squares: " + str(squares))

#list comprehension

squares = [value**2 for value in range(1,11)]
print(squares)