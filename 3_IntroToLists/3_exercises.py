
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