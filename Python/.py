def count_down(n):
    counter = []
    for x in range(n, -1, -1):
        counter.append(x)
    print(counter)  
count_down(99)

def printandreturn(a):
    print(a[0])
    return(a[1])
printandreturn([5,6])

def first_plus_length(a):
    sumoffandl = ((a[0]) + len(a))
    print(sumoffandl)
first_plus_length([1,2,3,4,5,6])

def values_greater_than_second(a):
    greaterthan = []
    for x in range(len(a)):
        if a[x] > a[1]:
            greaterthan.append(a[x])
    print(len(greaterthan))
    print(greaterthan)
    print(len(greaterthan) >= 2)
values_greater_than_second([3,5,1,8,2])


def this_length_that_value(size, value):
    givensize = []
    for x in range(size):
        givensize.append(value)
    print(givensize)
this_length_that_value(9,1)