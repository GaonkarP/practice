class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        mylis = []
        strnum = str(A)

        strnum[1:4:]

        for i in range(len(strnum)):
            mylis.append(strnum[i])

        finalli = []
        finalli.remove

        for i in range(len(strnum)):
            finalli.append(mylis[i])
            for j in range(len(strnum)):
                for k in range(len(strnum)):
                    print(strnum[i+j:k+1])

        return 1

myobj = Solution

# myobj.solve(myobj, 3245)

mystr = "decoraters starts here h h h  h"
print(mystr)

mylist = list(mystr)
print(mylist)
myset = set(mylist)

print(myset)

print(myset[3])