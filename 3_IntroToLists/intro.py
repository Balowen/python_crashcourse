bicycles = ['trek', 'cannondale', 'redline','specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
message2 = "I'd like to own a " + bicycles[3].title() + " bike."
print(message)
#append adds to the end of the list
bicycles.append('ducati')
print(bicycles)

#you can build list dynamically
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
#inserting into a list
motorcycles.insert(0, 'romet')
print(motorcycles)

#removing and item Using del
del motorcycles[0]
print(motorcycles)

#removing items using pop()
print("USING POP()")
#popping from top of a stack (end of a list)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
