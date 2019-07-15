cars = ['bmw', 'audi','polonez', 'toyota']
cars.sort()
print(cars)
#sort() irreversibly changes a list
cars.sort(reverse=True)
print(cars)

#sorted doesn't
print("Original list:")
print(cars)
print("Sorted list:")
print(sorted(cars))
print("Original list again")
print(cars)
print("\nREVERSE()")
cars = ['bmw', 'audi','polonez', 'toyota']
print(cars)
cars.reverse()
print(cars)

print("Length of list 'cars' is " + str(len(cars)))
