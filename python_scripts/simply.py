import random
import time
import types


def lottery():
    # returns 6 numbers between 1 and 40
    # for i in range(6):
    #     yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

# for random_number in lottery():
#        print("And the next number is... %d!" %(random_number))

print(list(lottery()))


def timeTaken(func):
    print(f"in time taken")
    def calctime(*args, **kwargs):
        print(f"in calc")
        t1 = time.time()
        retvalue = func(*args, **kwargs)
        t2 = time.time()
        print(f"\n\ntimeTaken is {t2 - t1} ms")

        return retvalue
    print(f"in time taken end")
    return calctime

@timeTaken
def funFib(fibBase=1, length = 10):    
    print("In funFib")
    fibseries = []

    fibseries.append(0)
    fibseries.append(1)

    # print(f"Type first 2 numbers of fib series whose sum is {fibBase}")
    # for _ in range(2):
    #     fibseries.append(int(input()))
    
    if fibseries[0] + fibseries[1] == fibBase:
        print(f"printing fib series of lenth {length}")
        print(f"fib series {fibseries}", end=",")
        for i in range(2, length):
            # fibseries[i] = fibseries[i-2] + fibseries[i-1]
            fibseries.append(fibseries[i-2] + fibseries[i-1])
            # print(fibseries[i], end=",")
    else:
        print(f"given numbers does not match the base {fibBase}")
    return "I am done"

@timeTaken
def funFibGenerator(fibBase=1, length = 10):
    print("In funFibGenerator")
    fibseries = []
    fibseries.append(0)
    fibseries.append(1)
    print(fibseries.__len__())
    print(len(fibseries))
    # print(f"Type first 2 numbers of fib series whose sum is {fibBase}")
    # for _ in range(2):
    #     fibseries.append(int(input()))
    
    if fibseries[0] + fibseries[1] == fibBase:
        a = fibseries[0]
        b = fibseries[1]
        print(f"Fib series of lenth {length} -->{a}", end=",")
        print(f"{b}", end=",")
        for _ in range(length-2):
            temp = a + b
            # print(f"{temp}", end=",") 
            a = b
            b = temp
            # fibseries[i] = fibseries[i-2] + fibseries[i-1]
            # fibseries.append(fibseries[i-2] + fibseries[i-1])
    else:
        print(f"given numbers does not match the base {fibBase}")

    return "I am done"

# print(funFibGenerator(length=9000)) ##--> return value of decorater is replaced wiht  funFibGenerator

exstring = "decoraters starts here h h h  h"

print("decoraters starts here h h h  h")

funFibGenerator()


# timeTaken(funFibGenerator) = @timeTaken




print("-------******--------")

def fibpropergen(first=0, second=1, n=10):
    temp = 0
    a, b = first, second
    print(__file__)
    print(__name__)
    print(__name__())
    

    while(a < 10):
        print(f"element nuber {temp}")
        yield a
        a, b = b, a+b


def fiblast():
    for value in fibpropergen():
        print(value)

print("---------------")

splitted = exstring.split()
print(exstring.split())
# splitted.extend("pra")
print(" ".join(splitted))


def total(initial = 5, *num, **key):
    count = initial

    print(initial)
    print(num)
    print(key)
    for n in num:
        count +=n

    for k in key:
        print(k)
        count += key[k]

    return count

print(total(100,2,3, clouds=50, stars=100))



import skill_test as st
# print(st.tasting.__name__)
# print(st.tasting())

# print(fiblast())

# print("---------------")
    
# mylist = "Configured version and local files version for tools/"

print("--------*******-------")

a = [1, 2, 3]
b = [7, 8, 9, 7]

mytup = {(i,j) for i in a for j in b}

class A: 
    def __init__(self, a):
        self.a = a
  
    # adding two objects
    def __add__(self, o):
        return self.a + o.a

class B:
    def __init__(self, a):
        self.a = a
  
    # adding two objects  
    def __add__(self, o): 
        return self.a + o.a + "from B" 



ob1 = A(1) 
ob2 = A(2) 
ob3 = A("Geeks") 
ob4 = B("For") 

mynum =round(30/7, 5) 
print(mynum)

testfun = lambda a, b, c: a+b+c

def mylamwrap(n=2):
    return lambda a : a**n


from copy import copy, deepcopy

mytestvar1 = "Anna P"
print(a)
b = copy(a)
mytestvar2 = mytestvar1
print(b)
b.append(6)
# b.pop(2)
print(a)
print(b)


  
# print(ob1 + ob2)

# print(ob3 + ob4)


# print({(i,j) for i in a for j in b})

# print({i: i*j for i in a for j in b})



# print(timeTaken(funFibGenerator)())
# funFibGenerator()

# print(type(fibpropergen()))
# print(fibpropergen())



# print(type(funFibGenerator()))

# mylist = [(1,3),(1,2),(1,4),(3,1),(4,2),(4,4),(1,4)]

# print(set(mylist))




# print(funFib(length=9000))

'''

# fill in this function
def fib():
    a, b = 4, 9
    while 1:
        yield a
        a, b = b, a + b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
    


'''

