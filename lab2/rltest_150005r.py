def ReverseList(InputList):
    if len(InputList) ==0:
        return []
    if type(InputList[0]) == list:
        return (ReverseList(InputList[1:])+[ReverseList(InputList[0])])
    else:
        return (ReverseList(InputList[1:])+[InputList[0]])

def rlTest():
    print ReverseList([ 1, 2, 3, 4, 5, 6])
    print ReverseList([ 1, 2, 'abc', 4, 5, 6] )
    print ReverseList([1, 2, [31, 32], 4, 5, 6] )
    print ReverseList([1, 2, [31, 32], 4, [51, [521, 522], 53], 6])
rlTest()    
     


                
