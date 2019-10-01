from PBST_150005R import*

BTree=CreateBinaryTree([])
Elements=[1,2,3,4,5,6,7,8,9,10]
for i in Elements:
    AddValue(BTree,i)


print "Search Value:",SearchValue(BTree,50)


searchval = SearchValue(BTree,9)
print "Search Value : ",searchval.value


PrintTree(BTree)

print "Delete Value :",DeleteValue(BTree,4)
PrintTree(BTree)

addingValue=15
print "Add new value : ",addingValue
AddValue(BTree,addingValue)
PrintTree(BTree)
