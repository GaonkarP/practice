import os
import time
'''

def time_taken(func):
    def calc_timetaken(*args, **kwargs):
        t1 = time.time()
        rtvalue = func(*args, **kwargs)
        t2 = time.time()
        print(f"time taken is {t2 - t1} mili seconds")

        return rtvalue
    return calc_timetaken

def sort_fun(n):

    myList = []
    for _ in range(n):
        try:
            myList.append(int(input("type number:")))

        except Exception as es:
            print(f"type a valid number\n {es}") 

    print(sorted(myList, reverse=True))


@time_taken
def multiplyNum(num):
    for i in range(num):
        print(f"number {num} multiply by {i} = {num*i}")

multiplyNum(100)


# decorator function to capitalize names
def names_decorator(function):
    def wrapper(arg1, arg2):
        arg1 = arg1.capitalize()
        arg2 = arg2.capitalize()
        string_hello = function(arg1, arg2)
        print(string_hello)
    #     return string_hello
    return wrapper

@names_decorator
def say_hello(name1, name2):
    return 'Hello ' + name1 + '! Hello ' + name2 + '!'

say_hello('sara', 'ansh') 	 # output => 'Hello Sara! Hello Ansh!'



my_tuple = ('sara', 6, 5, 0.97)
my_list = ['sara', 6, 5, 0.97]

print(my_tuple[0])     # output => 'sara'
print(my_list[0])     # output => 'sara'

# my_tuple[0] = 'ansh'    # modifying tuple => throws an error
my_list[0] = 'ansh'    # modifying list => list modified

print(my_tuple[0])     # output => 'sara'
print(my_list[0])     # output => 'ansh'


a = [1, 2, 3]
b = [7, 8, 9]


print([(x , y) for(x, y) in zip(a, b)])



class myEx():

    def __init__(self, var1, var2):
        self.variable1 = var1
        self.variable2 = var2
        self.joinedvar = zip(var1, var2)

    def myPrint(self):
        print(f"printing variable 1 {self.variable1} and variable 2 {self.variable2} and cancatenation {list(self.joinedvar)}")


obj1 = myEx("oh Hello!", " Praveen....!")

obj1.myPrint()


tlambda = lambda a, b : str(a)+str(b)

print((tlambda(2, "ten")))
'''


def tasting():
    print(__name__)