class Tree:
    def __init__(self, node, left, right) :
        self.node = node
        self.left = left
        self.right = right

    def addTree(self, node, left, right) :
        if self.node == None :
            self.node = node

        if self.node == node :
            if left == None :
                self.left = None
            else :
                self.left = Tree(left, None, None)
            
            if right == None :
                self.right = None
            else :
                self.right = Tree(right, None, None)
                
            return True 
        else : # find the node in the tree.
            if self.left != None :
                flag = self.left.addTree(node, left, right)
            else :
                flag = False
            
            if flag == True :
                return True
            else :
                if self.right != None :
                    flag = self.right.addTree(node, left, right)
                else :
                    flag = False
                    
                if flag == True :
                    return True
                else :
                    return False


def preorder(tree) :
    '''
    Root -> L -> R
    '''
    result = []
    result.append(tree.node) # Root
    
    if tree.left != None : # Left
        result = result + preorder(tree.left)
    
    if tree.right != None : # Right
        result = result + preorder(tree.right)

    return result

def inorder(tree) :
    '''
    L -> Root -> R
    '''
    result = []

    if tree.left != None : # Left
        result = result + inorder(tree.left)
    
    result.append(tree.node) # Root
    
    if tree.right != None : # Right
        result = result + inorder(tree.right)
    
    return result

def postorder(tree) :
    '''
    L -> R -> Root
    '''
    result = []
    
    if tree.left != None : # Left
        result = result + postorder(tree.left)
    
    if tree.right != None : # Right
        result = result + postorder(tree.right)
        
    result.append(tree.node) # Root

    return result

def getHeight(tree) :
# 
#   the height of the root is 1.
# 
    if tree == None :
        return 0
    else :

        # leftHeight = 1
        # rightHeight = 1

        # if tree.left != None :
        #     leftHeight = 1 + getHeight(tree.left)
        # else : # Be careful! Do not reference before assignment.
        #     return leftHeight
        
        # if tree.right != None :
        #     rightHeight = 1 + getHeight(tree.right)
        # else :
        #     return rightHeight

        # if leftHeight > rightHeight :
        #     return leftHeight
        # else :
        #     return rightHeight  
        
        
        leftHeight = getHeight(tree.left)
        rightHeight = getHeight(tree.right)

        if (leftHeight > rightHeight) :
            return leftHeight + 1
        else :
            return rightHeight +1


def main() :
    myTree = Tree(None, None, None)
    nodes = int(input()) # the number of the nodes

    for i in range(nodes) :
        myList = [int(v) for v in input().split()]

        if myList[1] == -1 :
            myList[1] = None

        if myList[2] == -1 :
            myList[2] = None

        # node : myList, left child : myList[1], right child : myList[2]
        # 5         : numbers
        # 1 2 3     : root(1), left child(2), right child(3)
        # 2 4 5     : node(2), left child(4), right child(5)
        # 3 -1 -1   : node(3), no child
        # 4 -1 -1   : node(4), no child
        # 5 -1 -1   : node(5), no child
        myTree.addTree(myList[0], myList[1], myList[2])

    print(*preorder(myTree))
    print(*inorder(myTree))
    print(*postorder(myTree))
    print(getHeight(myTree))

if __name__ == "__main__":
    main()
