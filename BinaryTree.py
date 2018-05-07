class Tree:
    def __init__(self, index, left, right) :
        self.index = index
        self.left = left
        self.right = right

    def addNode(self, index, left, right) :
        # root node == index
        if self.index == None :
            self.index = index

        if self.index == index :

            if left == None :
                self.left = None
            else :
                self.left = Tree(left, None, None)
            
            if right == None :
                self.right = None
            else :
                self.right = Tree(right, None, None)
                
            return True 
        else :
            if self.left != None :
                flag = self.left.addNode(index, left, right)
            else :
                flag = False
            
            if flag == True :
                return True
            else :
                if self.right != None :
                    flag = self.right.addNode(index, left, right)
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
    
    result.append(tree.index)
    
    if tree.left != None :
        result = result + preorder(tree.left)
    
    if tree.right != None :
        result = result + preorder(tree.right)

    return result

def inorder(tree) :
    '''
    L -> Root -> R
    '''
    result = []

    if tree.left != None :
        result = result + inorder(tree.left)
    
    result.append(tree.index)
    
    if tree.right != None :
        result = result + inorder(tree.right)
    
    return result

def postorder(tree) :
    '''
    L -> R -> Root
    '''
    result = []
    
    if tree.left != None :
        result = result + postorder(tree.left)
    
    if tree.right != None :
        result = result + postorder(tree.right)
        
    result.append(tree.index)

    return result

def getHeight(tree) :

    return 0

def main():
    myTree = Tree(None, None, None)

    n = int(input())

    for i in range(n) :
        myList = [int(v) for v in input().split()]

        if myList[1] == -1 :
            myList[1] = None

        if myList[2] == -1 :
            myList[2] = None

        myTree.addNode(myList[0], myList[1], myList[2])

    print(*preorder(myTree))
    print(*inorder(myTree))
    print(*postorder(myTree))
    print(getHeight(myTree))

if __name__ == "__main__":
    main()
