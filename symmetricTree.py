'''
Symmetric Tree(대칭 이진트리) https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/
주어진 이진트리가 좌우 대칭임을 판단하는 프로그램을 작성하시오. 예를 들어, 다음의 트리는 대칭이다.
대칭트리 예제
      1
    /  ⟍   
  2       2
 / ⟍    /  ⟍
4   3   3   4

하지만 다음의 트리는 대칭이 아니다.
비대칭트리 예제
      1
    /  ⟍   
  2       2
 /      /  
3      3   
'''


# Python program to check if a given Binary Tree is
# symmetric or not

# Node structure
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def isSymmetric(leftSubTree, rightSubTree):
    # If both trees are empty, then they are mirror images
    if leftSubTree is None and rightSubTree is None:
        return True

    """ 
    For two trees to be mirror images, the following three 
    conditions must be true 
    1 - Their root node's key must be same 
    2 - left subtree of left tree and right subtree 
        of the right tree have to be mirror images 
    3 - right subtree of left tree and left subtree 
        of right tree have to be mirror images 
    """

    if leftSubTree is not None and rightSubTree is not None:
        if leftSubTree.value == rightSubTree.value:
            return (isSymmetric(leftSubTree.left, rightSubTree.right) and
                    isSymmetric(leftSubTree.right, rightSubTree.left))

    # If neither of the above conditions is true then root1
    # and root2 are not mirror images
    return False


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)

    if root == None:
        print("Yes")
    elif isSymmetric(root.left, root.right) == True:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
