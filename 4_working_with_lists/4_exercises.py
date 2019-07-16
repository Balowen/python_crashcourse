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
