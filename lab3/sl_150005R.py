def skylineValue(Buildings,firstValue,lastValue):
    if firstValue==lastValue:
        return [(Buildings[firstValue][0],Buildings[firstValue][1]),(Buildings[firstValue][2],0)]
    else:
        mid=(firstValue+lastValue)/2
        Value1=skylineValue(Buildings,firstValue,mid)
        Value2=skylineValue(Buildings,mid+1,lastValue)
        M=Skyline(Value1,Value2)
        return M
    
def Skyline(Value1,Value2):
    Skyline=[]
    Skyline.append((-1,-1))
    Value1.append((float('inf'),-1))
    Value2.append((float('inf'),-1))
    i=0
    j=0
    height1 = 0
    height2 = 0
    n1=len(Value1)
    n2=len(Value2)
    while i<n1 and j<n2 :
        if Value1[i][0]==Value2[j][0]:
            height1=Value1[i][1]
            height2=Value2[j][1]
            if Skyline[-1][1]!=max(height1,height2):
                Skyline.append((Value1[i][0],max(height1,height2)))       
            i+=1
            j+=1            
        elif Value1[i][0] < Value2[j][0]:
            height1 = Value1[i][1]
            if Skyline[-1][1]!=max(height1,height2):
                Skyline.append((Value1[i][0],max(height1,height2)))
            i+=1
        elif Value2[j][0] < Value1[i][0]:
            height2 = Value2[j][1]
            if Skyline[-1][1]!=max(height1,height2):
                Skyline.append((Value2[j][0],max(height1,height2)))
            j+=1
    while i<n1:
        Skyline.append((Value1[i][0],Value1[i][1]))
        i+=1
    while j<n2:
        Skyline.append((Value2[j][0],Value2[j][1]))
        j+=1                     
    del Skyline[0]
    del Skyline[-1]
    

    return Skyline

def FindSkyline (Buildings):
    firstValue=0;
    lastValue=len(Buildings)-1
    Output=skylineValue(Buildings,firstValue,lastValue)
    return Output
    
