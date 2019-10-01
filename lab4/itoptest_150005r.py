def InfixtoPostfix(list1):
    list1.append(" ")
    postfix=[]
    stack=[]
    for i in list1:
        try:
            postfix.append(int(i))

        except:
            if len(stack)>0 and stack[-1]=="^":
                postfix.append("^")
                del stack[-1]
            if i=="+":
                while len(stack)>0 and (stack[-1]=="*" or stack[-1]=="/"):
                    postfix.append(b[-1])
                    del stack[-1]
            elif i==" ":
                for j in stack[::-1]:
                    postfix.append(j)
            
            if not i==")":
                stack.append(i)
            
            if i==")":
                while not stack[-1]=="(":
                    postfix.append(stack[-1])
                    del stack[-1]
                else:
                    del stack[-1]
            

    print postfix
InfixtoPostfix([12,"+",5])
InfixtoPostfix([92,"+",'(',24,"-",2,'*','(',5,'+',2,")",")",'*',10])
    
    
    
            
        

