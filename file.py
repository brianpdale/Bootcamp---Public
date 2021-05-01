num1 = 42 # variable declaration, number int
num2 = 2.3 # variable declaration, num float
boolean = True # Boolean
string = 'Hello World' # string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary
fruit = ('blueberry', 'strawberry', 'banana') # list
print(type(fruit)) # type check
print(pizza_toppings[1]) # list, access value
pizza_toppings.append('Mushrooms') # list, add value
print(person['name']) # dictionary, access value
person['name'] = 'George' # dictionary, change value
person['eye_color'] = 'blue', # dictionary, add value
print(fruit[2]) # list, access value

if num1 > 45: ### conditional, if
    print("It's greater")
else:           ### conditional, else
    print("It's lower")

if len(string) < 5: ### conditional, if
    print("It's a short word!")
elif len(string) > 15:  ### conditional, else if
    print("It's a long word!")
else:                   ### conditional, else
    print("Just right!")

for x in range(5):          """
    print(x)
for x in range(2,5):    for loop
    print(x)
for x in range(2,10,3):
    print(x)                """
x = 0               # variable decleration
while(x < 5):       # while loop
    print(x)
    x += 1          

pizza_toppings.pop()    ### list, delete value
pizza_toppings.pop(1)   ### list, delete value

print(person)           #dictionary, access value
person.pop('eye_color') #dictionary, delete value
print(person)           #dictionary, access value

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': E #conditional if
        continue                #continue
    print('After 1st if statement')
    if topping == 'Olives':     #conditional if
        break                    # break

def print_hello_ten_times():     # function 
    for num in range(10):       # argument,  for loop
        print('Hello')          # return

print_hello_ten_times()

def print_hello_x_times(x):      # function 
    for num in range(x):        # argument,  for loop
        print('Hello')      # return

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):      # function 
    for num in range(x):           # argument,  for loop
        print('Hello')              # return

print_hello_x_or_ten_times()        # return
print_hello_x_or_ten_times(4)       # return


"""
Bonus section
"""

# print(num3)                       # return
# num3 = 72                         # variable declreration
# fruit[0] = 'cranberry'            # TypeError: 'tuple' object does not support itme assignment
# print(person['favorite_team'])    # KeyError: 'favorite team'
# print(pizza_toppings[7])          # Index Error: list index our of range
#   print(boolean)                  # unexpected indent
# fruit.append('raspberry')         # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)                      # AttributeError: 'tuple' object has no attribute 'pop'