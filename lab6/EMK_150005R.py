from Heap_150360A import *
def ExtractMaxK(NumberList,k):
    kHeap=HeapBuildMaxHeap(NumberList)
    kHeap=kHeap[:min(len(NumberList),2**k)]
    kLargest=[]
    for i in xrange(k):
        kLargest.append(HeapExtractMax(kHeap))
    return kLargest
myHeap2 = ['Empty', 2, 4, 6, 8, 10, 12, 14, 98, 7, 5, 5, 3, 1,23,45,1,2,10,100,5,6,78]    
print ExtractMaxK(myHeap2,5)
