#dimensions of rectangle
dimensions = (200, 50)  #tuples are immutable lists

# dimensions[0] = 250    it won't work, can't change an item in a tuple
print(dimensions[0])
print(dimensions[1])

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#4_13 Buffet
foods = ('pizza','burger','kebab','falafel','fish')
print("menu:")
for item in foods:
    print(item)

foods = ('pizza','burger','hot-dog','chips','fish')
print("new menu:")
for item in foods:
    print(item)