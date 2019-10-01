def HeapParent(i):
  return i/2

def HeapLeft(i):
  return 2*i

def HeapRight(i):
  return 2*i + 1

def HeapMax(A):
  return A[1]

def HeapMaxHeapify(A, i):
  largest = i
  heap_size = len(A)-1
  l = HeapLeft(i)
  r = HeapRight(i)
  if (l <= heap_size and A[l] > A[i]):
    largest = l
  if (r <= heap_size and A[r] > A[largest]):
    largest = r
    
  if(largest != i):
    (A[i], A[largest]) = (A[largest], A[i])
    HeapMaxHeapify(A, largest)
  return A

def HeapBuildMaxHeap(A):
  heap_size = len(A)-1
  for i in range(heap_size/2, 0, -1):
    HeapMaxHeapify(A, i)
  return A

def HeapExtractMax(A):
  #Complete this method to extract(remove and return) the max element and rearrange the heap
  #A dummy implementation is provided
  if(len(A)<2):
      return None
  max_val = A[1]
  A[1]=A[-1]
  A.pop(-1)
  HeapMaxHeapify(A,1)
  return max_val
  
def HeapIncreaseKey(A, i, key):
  #Complete this method to increase the key value of the element at ith position and rearrange the heap
  #A dummy implementation is provided
  if((A[i]<key) or (A[i]=='-inf')):
    A[i]=key
  #HeapMaxHeapify(A,i)
    curnode=i
    while curnode!=1 and (A[HeapParent(curnode)]<A[curnode]):
        curnode=HeapParent(curnode)
        HeapMaxHeapify(A,curnode)
  return A

def HeapMaxHeapInsert (A, key):
  #Complete this method to insert the specified key value to the heap
  #A dummy implementation is provided
  A.append('-inf')
  HeapIncreaseKey(A,len(A)-1,key)
  return A
  
