


def sorting(n=10):

    print(f"Enter {n} integer numbers to be sorted")
    inList = []
    while(len(inList) < n):
        try:
            inList.append(int(input("Enter number : ")))

        except Exception as e:
            print(f"please enter the integer number {e}")

    print(f"numbers before sorting -->{inList}")
    # print(f"numbers soterd in reverse -->{inList.sort(reverse=True)}")
    print(sorted(inList, reverse=True))

def palindrome(instr = "praveen"):
    mostr = instr[::-1]
    if instr == mostr:
        print("sequence is palindrome")
    else:        
        print("sequence is not palindrome")

palindrome("malayalam")


import numpy as np
arr = np.array([1,2,3,4,5])
p = np.percentile(arr, 50) #Returns 50th percentile, e.g. median
print(arr)
print(arr.argsort()[-3:][::-1])
# [-3:][::-1]


def pyfunc(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1))    
pyfunc(9)