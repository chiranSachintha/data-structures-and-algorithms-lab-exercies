def findOddNumber(NumberList):
    startIndex=0
    endIndex=len(NumberList)-1
    midValue=int((startIndex+endIndex/2))
    if endIndex<startIndex:
        return None
    if startIndex==endIndex:
        return NumberList[startIndex]
        
    else:
        if NumberList[midValue]==NumberList[midValue+1]:
            if NumberList[midValue]==NumberList[midValue-1]:
                NumberList.pop(midValue)
                NumberList.pop(midValue-1)
                return findOddNumber(NumberList)
            elif midValue%2!=0:
                return findOddNumber(NumberList[0:midValue])
            else:
                return findOddNumber(NumberList[midValue+2:len(NumberList)])
        elif NumberList[midValue]==NumberList[midValue-1]:
            if midValue%2!=0:
                return findOddNumber(NumberList[midValue+1:len(NumberList)])
            else:
                return findOddNumber(NumberList[0:midValue-1])
        else:
            return NumberList[midValue]
    
