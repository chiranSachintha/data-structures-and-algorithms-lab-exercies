from PBT_150005R import*

ElementList=[3,4,5,6,7,8]
NewElementList=[9,10,11,12,13,14,15]

BTree=CreateBinaryTree(ElementList)

ExpandBTree=ExpandBinaryTree(BTree,NewElementList)


print "InOrder", TraverseInOrder(ExpandBTree)
print "PreOrder", TraversePreOrder(ExpandBTree)
print "PostOrder", TraversePostOrder(ExpandBTree)
