# 1. TASK: print "Hello World"
print ("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print ("Hello" + name)
print("Hello" + "," + name)	# with a comma
print("Hello" + "+" +name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42

x = [99,4,2,5,-3]
print(x[:])
#the output would be [99,4,2,5,-3]
print(x[1:])
#the output would be [4,2,5,-3];
print(x[:4])
#the output would be [99,4,2,5]
print(x[2:3])
dog = ("Canis Familiaris", "dog", "carnivore", 12)
print(dog)
dog = dog + ("domestic",)
print(dog)
capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
print(str(capitals))
for x in "hello":
    print(x)
