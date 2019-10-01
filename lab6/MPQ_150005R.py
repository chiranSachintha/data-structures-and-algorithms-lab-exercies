from Heap_150360A import *

def MPQCreate():
  return []

def MPQCreate(A):
  return HeapBuildMaxHeap(A)

def MPQEnqueue(A, key):
  HeapMaxHeapInsert(A, key)

def MPQDequeue(A):
  return HeapExtractMax(A)

def MPQIncreasePriority(A, i, newKey):
  if(A[i]<newKey):
    HeapIncreaseKey(A, i, newKey)

def MPQDecreasePriority(A, i, newKey):
  if(A[i]>newKey):
    #Complete this method to decrease the key value of the element at ith position of the list and rearrange the queue as required.
    A[i]=newkey
    HeapMaxHeapify(A,i)
    
