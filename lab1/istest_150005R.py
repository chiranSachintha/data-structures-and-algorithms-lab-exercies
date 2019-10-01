def InsertionSort(NumberList):
    for j in range(1,len(NumberList)):
        key=NumberList[j]
        i=j-1
        while i>=0 and NumberList[i]>key:
            NumberList[i+1]=NumberList[i]
            i=i-1
        NumberList[i+1]=key
    return NumberList

def TestInsertionSort():
    print "input 1:[1,3,5,6,8,9]"
    print "output 1" ,InsertionSort([1,3,5,6,8,9])
    print 'input 2: [1,2,3,3,4,8,6,5]'
    print "output 2:", InsertionSort([1,2,3,3,4,8,6,5])
    print "input 3: [9,8,7,6,5,4,3,2]"
    print "output 2:",InsertionSort([9,8,7,6,5,4,3,2])
    print "input 4: [1,5,5,3,9,9,6,7]"
    print "output 2:",InsertionSort([1,5,5,3,9,9,6,7])
TestInsertionSort()
    
            
