import os
import shutil
import sys
import getpass

def cretelist(num):
    li2= []
    for i in range(0, 100):
        li2.append(int(i))

    li2.insert(50, -10)
    print(li2)

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


def printerror():
    print(f"[ERROR]:    ", end="")

    
    print(f"<---")

def number_sorting(num = 0):
    ''' Hi
    just checking    
    '''
    print(__file__)
    if num == 0:
        num = 10

    li1=[]
    li1 = [1, 4, 66, -9, -39, -88, 99, 66, 6, 55]
    print("enter input numbers")

    while len(li1) < num:
        try:
            li1.append(int(input()))
        
        except ValueError as err:
            print(f"error: {err}")
        except KeyboardInterrupt:
            print("exiting as there is a keyboard interrupt")
            sys.exit(-1)
    print(f"given numbers {li1}")

    li1.sort(reverse=True)
    li1 = sorted(li1, reverse=True)

    print(f"sorted numbers are -->{li1}")
    print(f"second least number is {li1[(len(li1) - 2)]}")
