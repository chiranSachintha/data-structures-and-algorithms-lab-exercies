class BTNode:
    def __init__(self, val):
        self.lChild = None
        self.rChild = None
        self.value = val

class BinaryTree:
    def __init__(self):
        self.root = None

def AddLeftChild (ParentNode, ChildValue):
    if(ParentNode.lChild != None):
        return -1
    ParentNode.lChild = BTNode(ChildValue)
    return 1

def AddRightChild (ParentNode, ChildValue):
    if(ParentNode.rChild != None):
        return -1
    ParentNode.rChild = BTNode(ChildValue)
    return 1

def GetLeftChild (Node):
    return Node.lChild

def GetRightChild (Node):
    return Node.rChild

def CreateBinaryTree (ElementList):
    BTobject = BinaryTree()
    if len(ElementList)==0:
        return BTobject
    BTobject.root=BTNode(ElementList[0])
    currentNode=BTobject.root
    NodeList=[]

    for i in xrange(0,len(ElementList)):
        lc=2*i+1
        rc=2*i+2

        if lc<len(ElementList):
            AddLeftChild(currentNode,ElementList[lc])
            NodeList.append(currentNode.lChild)
        if rc<len(ElementList):
            AddRightChild(currentNode,ElementList[rc])
            NodeList.append(currentNode.rChild)
        else:
            break
        currentNode=NodeList.pop(0)

            
    return BTobject
def ExpandBinaryTree (BinTree, NewElementList):
    
    if len(NewElementList)==0:
        return BinTree
    if BinTree.root==None:
        BinTree.root=BTNode(NewElementList.pop(0))
    NodeList=[]
    currentNode=BinTree.root

    while len(NewElementList)!=0:
        if currentNode.lChild==None:
            AddLeftChild(currentNode,NewElementList.pop(0))
        NodeList.append(currentNode.lChild)

        if len(NewElementList)==0:
            break

        if currentNode.rChild==None:
            AddRightChild(currentNode,NewElementList.pop(0))

        NodeList.append(currentNode.rChild)
        currentNode=NodeList.pop(0)
        
    return BinTree


def InOrder(currentNode,inOrder):
    if currentNode.lChild!=None:
        InOrder(currentNode.lChild,inOrder)
    inOrder.append(currentNode.value)
    if currentNode.rChild!=None:
        InOrder(currentNode.rChild,inOrder)
    return inOrder

def TraverseInOrder(BinTree):
    if BinTree.root==None:
        return None
    
    inOrder=[]
    return InOrder(BinTree.root,inOrder)



def PreOrder(currentNode,preOrder):
    preOrder.append(currentNode.value)
    if currentNode.lChild!=None:
        PreOrder(currentNode.lChild,preOrder)
    if currentNode.rChild!=None:
        PreOrder(currentNode.rChild,preOrder)
    return preOrder

def TraversePreOrder(BinTree):
    if BinTree.root==None:
        return None

    preOrder=[]
    return PreOrder(BinTree.root,preOrder)
   


def PostOrder(currentNode,postOrder):
    if currentNode.lChild!=None:
        PostOrder(currentNode.lChild,postOrder)
    if currentNode.rChild!=None:
        PostOrder(currentNode.rChild,postOrder)
    postOrder.append(currentNode.value)
    return postOrder

def TraversePostOrder(BinTree):
    if BinTree.root==None:
        return None

    postOrder=[]
    return PostOrder(BinTree.root,postOrder)

