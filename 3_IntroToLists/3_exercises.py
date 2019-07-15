
#3-4 Guest list
invitationList = ['Danny', 'Sunny', 'Fanny']

print("I'd like to invite you, " + invitationList[0].title() + ", to a dinner")
print("I'd like to invite you, " + invitationList[1].title() + ", to a dinner")
print("I'd like to invite you, " + invitationList[2].title() + ", to a dinner")

#3-5 Changing guest List
print(invitationList[0].title() + " can't make it")
invitationList.remove(invitationList[0])
invitationList.insert(0,"Kenny")
print(invitationList)
print("I'd like to invite you, " + invitationList[0].title() + ", to a dinner")
print("I'd like to invite you, " + invitationList[1].title() + ", to a dinner")
print("I'd like to invite you, " + invitationList[2].title() + ", to a dinner")
#for person in invitationList:
#   print("I'd like to invite you, " + person + ", to a dinner")
#Ex 3.6
print("Bigger table found")
invitationList.insert(0,"Elly")
invitationList.insert(1,"Joe")  #wrzuca na podany indeks
invitationList.append("Lasty")
print(invitationList)

for person in invitationList:
   print("I'd like to invite you, " + person + ", to a dinner")

#Ex 3.7
print("I can invite only 2 people for dinner")
personToGo  = invitationList.pop() #z konca
print("Sorry " + personToGo)
print(invitationList)
personToGo  = invitationList.pop() #z konca
print("Sorry " + personToGo)
print(invitationList)
personToGo  = invitationList.pop() #z konca
print("Sorry " + personToGo)
print(invitationList)
personToGo  = invitationList.pop() #z konca
print("Sorry " + personToGo)
print(invitationList)

for person in invitationList:
    print(person + " is still invited")
del invitationList[:]
print(invitationList)
print("dupa")

