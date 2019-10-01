from PBT_150005R import *

def BinarySearch(currentNode,Value,parentNode):
    if(currentNode.value == Value):
        return currentNode,"node",parentNode
    elif(currentNode.value>Value):
        if(currentNode.lChild!=None):
            return BinarySearch(currentNode.lChild,Value,currentNode)
        else:
            return currentNode,"left",parentNode
    else:
        if(currentNode.rChild!=None):
            return BinarySearch(currentNode.rChild,Value,currentNode)
        else:
            return currentNode,"right",parentNode
    
def AddValue (BinTree, NewValue):
    if (BinTree.root== None):
        BinTree.root=BTNode(NewValue)
    Node,position,pNode=BinarySearch(BinTree.root,NewValue,BinTree.root)
    if(position=="node"):
        return -1
    elif(position=="left"):
        AddLeftChild(Node,NewValue)
    else:
        AddRightChild(Node,NewValue)
    return 1

def SearchValue (BinTree, SearchingValue):
    if(BinTree.root == None):
        return None
    Node,position,pNode=BinarySearch(BinTree.root,SearchingValue,BinTree.root)
    if(position == "node"):
        return Node
    else:
        return None

def DeleteValue (BinTree, DelValue):
    node,position,pNode=BinarySearch(BinTree.root,DelValue,BinTree.root)
    if(position!="node"):
        return None
    Value=node.value
    if(node.lChild != None):
        currentNode=node.lChild
        parent=currentNode
        while(currentNode.rChild!=None):
            parent=currentNode
            currentNode=currentNode.rChild
        if(parent==currentNode):
            node.value=parent.value
            node.lChild=parent.lChild
        else:
            node.value=currentNode.value
            parent.rChild=currentNode.lChild
    elif(node.rChild != None):
        node.value=node.rChild.value
        node.lChild=node.rChild.lChild
        node.rChild=node.rChild.rChild
    else:
        if(node==BinTree.root):
           BinTree.root=None
        elif(pNode.lChild==node):
            pNode.lChild=None
        else:
            pNode.rChild=None
    return Value


def PrintTree (BinTree):
    SortedTree=TraverseInOrder(BinTree)
    for i in SortedTree:
        print i,
    print ""
    return 
