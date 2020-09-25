import os
import shutil
import sys
import getpass
import time



def time_taken(func):
    def calc_time(*args, **kwrgs):
        t1 = time.time()
        result = func(*args, **kwrgs)
        t2 = time.time()
        print(f"time taken is {t2 - t1} sec")
        return result
    return(calc_time)

def cretelist(num):
    li2= []
    for i in range(0, 100):
        li2.append(int(i))

    li2.insert(50, -10)
    print(li2)


@time_taken
def fibonaci_series(length = 0, maxnum = 0):
    if length != 0 or maxnum != 0 :
        a = 0
        b = 1
        total = sum([a,b])
        print(f"first total{total}")
        fib_ser = []
        fib_ser.append(a)
        fib_ser.append(b)
        if length != 0:
            for i in range(2, length):
                total = sum([a,b])
                fib_ser.append(total)
                a = b
                b = total

        elif maxnum != 0:
            while(total<= maxnum):
                a = b
                b = total
                fib_ser.append(total)
                total = sum([a,b])

            

        print(f"fibonacci series is {fib_ser}")
    else:
        print("please provide the range/max number")

def myprint(func):
    func()


@time_taken
def looong_int(num):
    for i in range(num):
        i = i*2

def printerror():
    print(f"[ERROR]:    ", end="")

    
    print(f"<---")

@time_taken
def number_sorting(num = 0):
    ''' Takes numbers from key board.
    default it takes 10 numbers
    could be controlled by parameter 'num'    
    '''
    print(__file__)
    print(f"given input is {num}")
    if num == 0:
        num = 10
    print(f"given input is {num}")
    li1=[]
    li1 = [1, 4, 66, -9, -39, -88, 99, 66, 88, 99]
    print("enter input numbers")

    while len(li1) < num:
        try:
            li1.append(int(input()))
        
        except ValueError as err:
            print(f"error: {err}")
        except KeyboardInterrupt:
            print("exiting as there is a keyboard interrupt")
            sys.exit(-1)
        else:
            pass
            # print("in else")
        finally:
            pass
            # print("in finally")
        # print("In while loop end")            

    print(f"given numbers {li1}")

    li1.sort(reverse=True)
    li1 = sorted(li1, reverse=True)

    ahha + bin
    annnn + 5 = 0

    
    print(f"sorted numbers are -->{li1}")
    print(f"second least number is {li1[(len(li1) - 2)]}")
