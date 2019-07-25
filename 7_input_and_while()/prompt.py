prompt = "Enter the city you have visited: "
prompt += "\n(Enter 'quit' whe you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print('City: ' + city.title())
