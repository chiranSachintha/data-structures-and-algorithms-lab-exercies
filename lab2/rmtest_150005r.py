import sys

def RecursiveMax(NumberList):
    if len(NumberList) == 0:
        return (-sys.maxsize -1)
    elif type(NumberList[0]) == list:
        return max(RecursiveMax(NumberList[0]), RecursiveMax(NumberList[1:])) 
    elif type(NumberList[0]) == int:
        return max(NumberList[0], RecursiveMax(NumberList[1:]))               
    else:
        return RecursiveMax(NumberList[1:])                                  

def rmTest():
    print "input series equal = [2, 4, 6, 8, [11, 9, 7], 5, 3, 1]"
    print "output = ",RecursiveMax([2, 4, 6, 8, [11, 9, 7], 5, 3, 1] )
    print "input series equal = [2, 4, 6, 8, [[11], 10, [9, 7]], 5, 3, 1]]"
    print "output = ", RecursiveMax([2, 4, 6, 8, [[11], 10, [9, 7]], 5, 3, 1])
    print "input series equal = [12, 4, 6, 'ssc', 8, 2, 'ncc', 10]]"
    print "output = ", RecursiveMax([12, 4, 6, 'ssc', 8, 2, 'ncc', 10] )
    print "input series equal = [1, 2, 3, 4, 5, 6]"
    print "output = ",RecursiveMax([ 1, 2, 3, 4, 5, 6])
rmTest()
    
    

    
