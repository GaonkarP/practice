
import os
import shutil
import sys
import getpass

import helper as hp




def changevalue(var1):
    var1 = 10

    return var1

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

class Bclass():

    def __init__(self, name, value):
        self.name = name
        self.value = value
    def myprint(self):
        print(f"input values name is {self.name}, corresponding value is {self.value}")
    

class C(Bclass):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def myprintC(self):
        print(f"input values from C clsass: name is {self.name}, corresponding value is {self.value}")
    
class D:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def myprintD(self):
        print(f"input values from D clsass: name is {self.name}, corresponding value is {self.value}")

def main():
    cwd = os.getcwd()
    # hp.number_sorting()
    hp.find_armstrong(153)
    #test commit removed

    # hp.looong_int(10000000)

    # hp.cretelist(100)
    # hp.fibonaci_series(maxnum= 8973978734)
    # print(hp.myprint)



    # test = hp.myprint(hp.printerror)


exit(main())
