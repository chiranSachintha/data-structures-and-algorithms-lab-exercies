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



    
