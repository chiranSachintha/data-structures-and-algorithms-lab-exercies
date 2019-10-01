def ValidateExpression(list1):
    list2=[]
    list3=["{","[","(","}","]",")"]
    for i in list1:
        if i in list3[:3]:
            list2.append(i)
        if i in list3[3:]:
            if len(list2)>0 and list3[(list3.index(i))%3]==list2[-1]:
                del list2[-1]
            else: return False

    return True
value=ValidateExpression([ '{', 2, '[', 4, '(', 6, ')', '+', 8, ']', '-', 2, '}' ] )
print value
            
            



