def InsertionSort(NumberList):
    for j in range(1,len(NumberList)):
        key=NumberList[j]
        i=j-1
        while i>=0 and NumberList[i]>key:
            NumberList[i+1]=NumberList[i]
            i=i-1
        NumberList[i+1]=key
    print NumberList
