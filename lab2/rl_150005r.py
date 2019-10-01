def ReverseList(InputList):
    if len(InputList) ==0:
        return []
    if type(InputList[0]) == list:
        return (ReverseList(InputList[1:])+[ReverseList(InputList[0])])
    else:
        return (ReverseList(InputList[1:])+[InputList[0]])





                
