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

def listsorting():    
    print("list sorting")

    li1=[]
    li1 = [1, 4, 66, -9, -39, -88, 99, 66, 6, 55]

    print("enter input numbers")
    # for i in range(0,10):
    #     li1.append(int(input()))
    print(f"given numbers {li1}")

    li1.sort(reverse=True)
    print(f"sorted numbers are -->{li1}")
    print(f"second least number is {li1[(len(li1) - 1)]}")
