class Solution:
    '''
    Problem Description
    For given number A find if its GOOD number or not.
    Return 0/1

    GOOD number:
        -A number can be broken into different contigous sub-sequence parts.
        -Suppose a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245 3245
        -And this number is a GOOD number, since product of every digit of a contigous subsequence is unique/different  

    '''

    # def __init__(self):
    #     pass
    # @param A : integer
    # @return an integer
    def solve(self, A):
        mylis = []
        strnum = str(A)
        finalli = []

        for i in range(len(strnum)):
            for j in range(i+1, len(strnum) + 1):
                finalli.append(strnum[i:j])
        finalli = list(set(finalli))
        print(finalli)
        mydict = {}
        prodlist=[]
        for i in range(len(finalli)):
            tempprod = 1
            for j in finalli[i]:
                tempprod *= int(j)
            mydict[int(finalli[i])] = tempprod
            prodlist.append(tempprod)
        print(mydict)
        prodlist = set(prodlist)
        if len(finalli) == len(prodlist):
            print(f"Given number {A} is GOOD")
            return 1
        else:
            print(f"Given number {A} is not GOOD")
            return 0
            
    def ordering(self, A):
        modString = A.split(" ")
        modString = list(set(modString))
        print(A)
        print(modString)
        finallist = []
        for i in range(len(modString) - 1):
            for j in range(i+1, len(modString)):
                firstword = modString[i]
                secondword = modString[j]
                # print("firstword--> " + firstword + ". secondword-->" + secondword)
                letteroccurance = 0
                templi = []
                if len(firstword) == len(secondword):
                    tempstr = firstword
                    for letter in secondword:
                        if tempstr.__contains__(letter):
                            tempstr = tempstr.replace(letter, "", 1)
                            letteroccurance += 1
                    if letteroccurance == len(firstword):
                        templi.append(i+1)
                        templi.append(j+1)
                        finallist.append(templi)

        print(finallist)


myobj = Solution()

# myobj.solve(234579)
# myobj.ordering("The only argument is the array of strings A.")
myobj.ordering("dog cat anna tac god act tact naan nana great again the farm arm gain cat dog")
