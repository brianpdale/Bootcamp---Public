print("----------Part I----------")
NAME=str(input("What is your name? "))
print("Your name is:",NAME)


print("----------Part II----------")
myname= "Brian"
NAME = ""
while NAME != myname:
    NAME = str(input("What is your name? "))
if NAME == myname:
    print("Hey, thats my name too!")


print("----------Part III----------")
namelist = []
for x in range(10):
    NAME = str(input("What is your name? "))
    namelist.append(NAME)
if len(namelist)  == 10:
    print("It was nice to meet all of you!")
    for elem in namelist:
        print("- " + elem)
        

print("----------Part IV----------")
names = []
while len(names) < 10: 
    NAME = str(input("What is your name? "))
    if NAME in (names):
        print("name already entered")
    else: names.append(NAME)
if len(names) == 10:
    print("It was nice to meet all of you!")
    for elem in names:
        print("- " + elem)

