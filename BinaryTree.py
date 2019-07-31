class Tree:
    def __init__(self, value, left, right) :
        self.root = value
        self.left = left
        self.right = right

    def addTree(self, value, left, right) :
        # 1. Find the value in the tree.
        # 2. Make the them(left and right) tree.
        
        if self.root == None :
            # Set the value as root if the tree is empty.
            self.root = value

        if self.root == value : # Found the value at root(level 0).
            if left == None :
                self.left = None
            else :
                self.left = Tree(left, None, None)
            
            if right == None :
                self.right = None
            else :
                self.right = Tree(right, None, None)

            return True 
            
        else : # Deep dive to find the value in the tree.
            if self.left != None :
                if self.left.addTree(value, left, right) == True :
                    return True
            else :
                if self.right != None :
                    if self.right.addTree(value, left, right) == True :
                        return True
            
            return False    

def preorder(tree) :
    '''
    Root -> L -> R
    '''
    result = []
    result.append(tree.root) # Root
    
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
    
    result.append(tree.root) # Root
    
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
        
    result.append(tree.root) # Root

    return result

def getHeight(tree) :
# 
#   the height of the root is 1.
# 
    if tree == None :
        return 0
    else :        
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

        # node      : myList, left child : myList[1], right child : myList[2]
        # 5         : numbers

        # 1 2 3     : root(1), left child(2), right child(3)
        # 2 4 5     : node(2), left child(4), right child(5)
        # 3 -1 -1   : node(3), no child
        # 4 -1 -1   : node(4), no child
        # 5 -1 -1   : node(5), no child
        
        # 1 2 3
        # 2 4 5
        # 3 -1 -1
        # 4 -1 -1
        # 5 -1 -1
        myTree.addTree(myList[0], myList[1], myList[2])

    print(*preorder(myTree))
    print(*inorder(myTree))
    print(*postorder(myTree))
    print(getHeight(myTree))

if __name__ == "__main__":
    main()
