for x in range(151):            # Basic - Print all integers from 0 to 150.
    print(x)


for y in range(0, 1000, 5):     # Multiples of Five - Print all the multiples of 5 from 5 to 1,000
    print(y)


z = 1
for z in range(1, 101):         # Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
    if z % 10 == 0:
        print("Coding Dojo")
    elif z % 5 == 0:
        print("Coding")
    else:
        print(z)


sum = 0
for i in range(500000):         # Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
    if i % 2 != 0:
        sum += i
    if i == 499999:
        print(sum)


for t in range (2018, 0, -4):   # Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
    print(t)


lowNum = 3                      # Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
highNum = 222
mult = 16
for flex in range(lowNum, highNum, mult):
        print(flex)







